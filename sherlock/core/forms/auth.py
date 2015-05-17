import logging
from django.contrib.auth import forms

logger = logging.getLogger(__name__)


class AuthenticationForm(forms.AuthenticationForm):
    def is_valid(self):
        success = super(AuthenticationForm, self).is_valid()

        for field, error in self.errors.items():
            if field != '__all__':
                self.fields[field].widget.attrs.update({'class': 'invalid'})
            else:
                self.fields['password'].widget.attrs.update({'class': 'invalid'})

        return success


class UserCreationForm(forms.UserCreationForm):
    pass
