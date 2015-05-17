from django import forms
from ..models import Submission, Clue, Hunt

class SubmissionForm(forms.ModelForm):
    clue = forms.SlugField()

    class Meta:
        model = Submission
        fields = ['image', 'comment']

class HuntForm(forms.ModelForm):
    class Meta:
        model = Hunt
        fields = ['name', 'description', 'start_time', 'end_time']

class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ['name', 'text', 'points']
