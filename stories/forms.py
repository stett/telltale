from django import forms
from django.conf import settings
from django.core.validators import EmailValidator
from django.core.mail import send_mail
from itertools import takewhile
from stories.models import Story, StoryChunk
from users.models import User
from users.services import generate_password


class StoryChunkWriteForm(forms.ModelForm):

    invitations = forms.CharField(required=False)

    class Meta:
        model = StoryChunk
        fields = ['content', 'leadin', 'published', 'invitations']

    def __init__(self, author, story=None, *args, **kwargs):
        super(StoryChunkWriteForm, self).__init__(*args, **kwargs)
        self.author = author._wrapped if hasattr(author, '_wrapped') else author
        self.story = story

        # Only require leadin if this is a new story or this is not the last chunk
        if (not story) or (story and story.chunks.count() < story.num_chunks - 1):
            self.fields['leadin'].required = True

    def clean_invitations(self):

        # Split invitations into a python list
        invitations = self.cleaned_data['invitations'].split(',')
        invitations = [invitation.strip() for invitation in takewhile(lambda i: len(i) > 0, invitations)]

        # Ensure that all the invitations are valid email addresses
        validate = EmailValidator(message="One or more of the invitations you wrote is not a valid email address.")
        for invitation in invitations:
            validate(invitation)

        # Make sure none of the invitations is the story manager...
        # that's cheating the system.
        if self.author.email in invitations:
            self.add_error('invitations', "You can't invite yourself, silly.")

        return invitations

    def clean(self):
        cleaned_data = super(StoryChunkWriteForm, self).clean()

        # Ensure that there aren't already too many chunks
        if self.story and self.story.chunks.count() >= self.story.num_chunks:
            self.add_error(None, "Story already has maximum number of chunks.")

        # Make sure the content is long enough
        content = cleaned_data.get('content')
        if content and len(content) < settings.MIN_STORY_CHUNK_SIZE:
            self.add_error('content', "Content must be at least %s characters long." % settings.MIN_STORY_CHUNK_SIZE)

        # If this isn't the last chunk, make sure there's a leadin
        if self.fields['leadin'].required:
            leadin = cleaned_data.get('leadin')
            if leadin and len(leadin) < settings.MIN_STORY_LEADIN_SIZE:
                self.add_error('leadin', "Lead-in must be at least %s characters long." % settings.MIN_STORY_LEADIN_SIZE)

        # If this is a new story, ensure that at least 2 users have been invited
        invitations = self.cleaned_data.get('invitations', [])
        if not self.story and len(invitations) < settings.MIN_STORY_AUTHOR_NUMBER - 1:
            self.add_error('invitations', "You must invite at least %s authors to join your story." % (settings.MIN_STORY_AUTHOR_NUMBER - 1))

        return cleaned_data

    def send_invitation_email(self, user, password=None):
        message = "Hello %s,\n\n%s has invited you to join a story at telltale.com. Click the link below to join in!" % (user.get_short_name(), self.author.get_full_name())
        if password:
            message += "\n\nYour temporary login password is: %s" % password
        send_mail("Telltale Story Invitation", message, self.author.email, [user.email], fail_silently=False)

    def save(self):

        # Create the story object if it doesn't already exist
        if not self.story:
            self.story = Story.objects.create(manager=self.author)
            self.story.authors.add(self.author)

        # Add users on the invite list
        invitations = self.cleaned_data.get('invitations', [])
        for invitation in invitations:

            # Get or create a user and send them an invite
            try:
                user = User.objects.get(email=invitation)
                self.send_invitation_email(user)
            except:
                password = generate_password()
                user = User.objects.create_user(
                    email=invitation,
                    password=password)
                self.send_invitation_email(user, password)

            # Add the user to the list of authors
            self.story.authors.add(user)

        # Make sure the instance has an author and story
        self.instance.author = self.author
        self.instance.story = self.story

        # Get the previous chunk
        prev_chunk = self.story.get_last_chunk()

        # Create the chunk
        chunk = super(StoryChunkWriteForm, self).save()

        # Connect this chunk to the last chunk in the story which doesn't have
        # a "next_chunk"
        if prev_chunk:
            prev_chunk.next_chunk = chunk
            prev_chunk.save()

        # If the story is finished, mark it as such. Otherwise, update the
        # story's current author.
        if (self.story.chunks.count() == self.story.num_chunks):
            self.story.mark_finished()
        else:
            self.story.update_current_author()

        # Return the chunk
        return chunk


class StoryJoinForm(forms.Form):
    pass
