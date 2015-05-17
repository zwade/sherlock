import logging
from django import forms
from django.contrib.auth.forms import AuthenticationForm
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


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta: 
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
