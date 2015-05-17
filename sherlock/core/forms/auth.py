import logging
from django.contrib.auth import forms
from django.contrib.auth.models import User

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
    class Meta: 
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2') 
