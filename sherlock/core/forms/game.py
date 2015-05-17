from django import forms
from django.utils import timezone
from ..models import Submission, Clue, Hunt

class SubmissionForm(forms.ModelForm):
    clue = forms.SlugField()
    comment = forms.CharField(required=False)

    class Meta:
        model = Submission
        fields = ['image', 'comment']

class HuntForm(forms.ModelForm):
    date_format = '%d %B, %Y'
    time_format = '%I:%M %p'

    start_time = forms.SplitDateTimeField(input_date_formats=[date_format], input_time_formats=[time_format])
    end_time = forms.SplitDateTimeField(input_date_formats=[date_format], input_time_formats=[time_format])

    class Meta:
        model = Hunt
        fields = ['name', 'description', 'start_time', 'end_time']

    def __init__(self, data=None, *args, **kwargs):
        if data:
            if 'start_time' in data:
                normdate = data['start_time'].astimezone(timezone.get_current_timezone())
                data['start_time_0'] = normdate.strftime(self.date_format)
                data['start_time_1'] = normdate.strftime(self.time_format)
            if 'end_time' in data:
                normdate = data['end_time'].astimezone(timezone.get_current_timezone())
                data['end_time_0'] = normdate.strftime(self.date_format)
                data['end_time_1'] = normdate.strftime(self.time_format)
        super(HuntForm, self).__init__(data, *args, **kwargs)

class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ['name', 'text', 'points']
