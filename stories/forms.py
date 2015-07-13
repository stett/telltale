from django import forms
from django.conf import settings
from stories.models import Story, StoryChunk


class StoryChunkWriteForm(forms.ModelForm):
    class Meta:
        model = StoryChunk
        fields = ['content', 'leadin', 'published']

    def __init__(self, author, story=None, **kwargs):
        super(StoryChunkWriteForm, self).__init__(**kwargs)
        self.author = author
        self.story = story

    def clean(self):
        cleaned_data = super(StoryChunkWriteForm, self).clean()

        # Ensure that the leadin position isn't past the end of the content
        if cleaned_data['leadin_position'] >= len(cleaned_data['content']):
            self.add_error(
                'leadin_position',
                "Lead-in must start before end of content block.")

        # Ensure that there aren't already too many chunks
        if self.story and self.story.chunks.count() >= settings.STORY_CHUNK_NUMBER:
            self.add_error(None, "Story already has maximum number of chunks.")

        return cleaned_data

    def save(self):

        import ipdb; ipdb.set_trace()

        # Create the story object if it doesn't already exist
        if not self.story:
            self.story = Story.objects.create(manager=self.author)

        # Make sure the instance has an author and story
        self.instance.author = self.author
        self.instance.story = self.story

        # Connect this chunk to the last chunk in the story which doesn't have
        # a "next_chunk"
        self.instance.prev_chunk = self.story.get_last_chunk()

        # Create the chunk
        chunk = super(StoryChunkWriteForm, self).save()

        # Return the chunk
        return chunk


class StoryJoinForm(forms.Form):
    pass
