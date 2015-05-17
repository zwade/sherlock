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
        widgets = {
            "start_time": forms.SplitDateTimeWidget(),
            "end_time": forms.SplitDateTimeWidget()
        }

class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ['name', 'text', 'points']
