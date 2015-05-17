import logging
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from ..forms.auth import AuthenticationForm, UserCreationForm

logger = logging.getLogger(__name__)


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("index")
        return render(request, 'login.html', {'form': AuthenticationForm()})

    def post(self, request):
        form = AuthenticationForm(None, request.POST)

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.GET.get('next', 'index')

            return redirect(next_url)

        return render(request, 'login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("index")
        return render(request, 'register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # Login the created user

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)

            return redirect("index")

        return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("index")
