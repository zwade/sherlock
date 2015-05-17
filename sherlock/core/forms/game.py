from django import forms
from ..models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['image', 'comment']

class ClueForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ClueForm, self).__init__(post, *args, **kwargs)

class HuntForm(forms.Form):
    pass

class NewClueForm(forms.Form):
    pass
