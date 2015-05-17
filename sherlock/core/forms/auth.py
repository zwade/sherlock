import logging
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class AuthenticationForm(AuthenticationForm):
    def is_valid(self):
        success = super(AuthenticationForm, self).is_valid()

        for field, error in self.errors.items():
            if field != '__all__':
                self.fields[field].widget.attrs.update({'class': 'invalid'})
            else:
                self.fields['password'].widget.attrs.update({'class': 'invalid'})

        return success


class UserCreationForm(UserCreationForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')
