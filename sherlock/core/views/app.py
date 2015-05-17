import logging
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .auth import LoginView
from . import LoginRequiredMixin

logger = logging.getLogger(__name__)

def index_view(request):
    if not request.user.is_authenticated():
        return render(request, "splash.html")
    return render(request, "hunts.html")

class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user_settings.html', {'chpw': PasswordChangeForm(request.user)})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'user_settings.html', {'chpw': form})
