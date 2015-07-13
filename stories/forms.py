from django import forms
from stories.models import Story, StoryChunk


class StoryChunkWriteForm(forms.ModelForm):
    class Meta:
        model = StoryChunk
        fields = ['content', 'leadin_position', 'published']

    def __init__(self, author, story=None, **kwargs):
        super(StoryChunkWriteForm, self).__init__(**kwargs)
        self.author = author
        self.story = story

    def clean(self):
        cleaned_data = super(StoryChunkWriteForm, self).clean()
        """
        TODO: Ensure the story isn't already complete,
              and other stuff like that.
        """
        return cleaned_data

    def get_story(self):
        if not self.story:
            self.story = Story.objects.create(manager=self.author)
        return self.story

    def save(self):

        # Make sure the instance has an author and story
        self.instance.author = self.author
        self.instance.story = self.get_story()

        # Create the chunk
        chunk = super(StoryChunkWriteForm, self).save()

        # Return the chunk
        return chunk


class StoryJoinForm(forms.Form):
    pass
