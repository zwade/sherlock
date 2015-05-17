from django import forms
from ..models import Submission, Clue, Hunt

class SubmissionForm(forms.ModelForm):
    clue = forms.SlugField()
    comment = forms.CharField(required=False)

    class Meta:
        model = Submission
        fields = ['image', 'comment']

class HuntForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(input_date_formats=['%d %B, %Y'], input_time_formats=['%I:%M %p'])
    end_time = forms.SplitDateTimeField(input_date_formats=['%d %B, %Y'], input_time_formats=['%I:%M %p'])

    class Meta:
        model = Hunt
        fields = ['name', 'description', 'start_time', 'end_time']

class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ['name', 'text', 'points']
