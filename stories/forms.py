from django import forms
from django.conf import settings
from stories.models import Story, StoryChunk


class StoryChunkWriteForm(forms.ModelForm):

    invitations = forms.CharField(required=False)

    class Meta:
        model = StoryChunk
        fields = ['content', 'leadin', 'published', 'invitations']

    def __init__(self, author, story=None, *args, **kwargs):
        super(StoryChunkWriteForm, self).__init__(*args, **kwargs)
        self.author = author._wrapped if hasattr(author, '_wrapped') else author
        self.story = story

    def clean_invitations(self):
        invitations = self.cleaned_data['invitations']
        invitations = [invitation.strip() for invitation in invitations.split(',')]
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
        if self.story and self.story.chunks.count() < self.story.num_chunks - 1:
            leadin = cleaned_data.get('leadin')
            if leadin and len(leadin) < settings.MIN_STORY_LEADIN_SIZE:
                self.add_error('leadin', "Lead-in must be at least %s characters long." % settings.MIN_STORY_LEADIN_SIZE)

        return cleaned_data

    def save(self):

        # Create the story object if it doesn't already exist
        if not self.story:
            self.story = Story.objects.create(manager=self.author)
            self.story.authors.add(self.author)

        # Add users on the invite list
        if self.invitations:
            import ipdb; ipdb.set_trace()

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
