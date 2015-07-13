from django import forms
from django.conf import settings
from stories.models import Story, StoryChunk


class StoryChunkWriteForm(forms.ModelForm):
    class Meta:
        model = StoryChunk
        fields = ['content', 'leadin', 'published']

    def __init__(self, author, story=None, *args, **kwargs):
        super(StoryChunkWriteForm, self).__init__(*args, **kwargs)
        self.author = author._wrapped if hasattr(author, '_wrapped') else author
        self.story = story

    def clean(self):
        cleaned_data = super(StoryChunkWriteForm, self).clean()

        # Ensure that there aren't already too many chunks
        if self.story and self.story.chunks.count() >= settings.STORY_CHUNK_NUMBER:
            self.add_error(None, "Story already has maximum number of chunks.")

        return cleaned_data

    def save(self):

        # Create the story object if it doesn't already exist
        if not self.story:
            self.story = Story.objects.create(manager=self.author)
            self.story.authors.add(self.author)

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

        # Return the chunk
        return chunk


class StoryJoinForm(forms.Form):
    pass
