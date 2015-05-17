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
        widgets = {
            'start_time': forms.SplitDateTimeWidget(date_format='%d %B, %Y', time_format='%I:%M %p'),
            'end_time': forms.SplitDateTimeWidget(date_format='%d %B, %Y', time_format='%I:%M %p'),
        }

    def __init__(self, data=None, *args, **kwargs):
        if data:
            if 'start_time' in data:
                dec = self.Meta.widgets['start_time'].decompress(data['start_time'])
                data['start_time_0'] = dec[0]
                data['start_time_1'] = dec[1]
            if 'end_time' in data:
                dec = self.Meta.widgets['end_time'].decompress(data['end_time'])
                data['end_time_0'] = dec[0]
                data['end_time_1'] = dec[1]
        super(HuntForm, self).__init__(data, *args, **kwargs)

class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ['name', 'text', 'points']
