from django import forms
from stories.models import Story, StoryChunk


class StoryChunkWriteForm(forms.ModelForm):
    class Meta:
        model = StoryChunk
        fields = ['content', 'leadin_position']


class StoryJoinForm(forms.Form):
    pass
