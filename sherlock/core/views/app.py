import logging
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .auth import LoginView
from . import LoginRequiredMixin

logger = logging.getLogger(__name__)


@login_required
def index_view(request):
    joined_hunts = request.user.joined_hunts.all()
    active_hunts = [h for h in joined_hunts if h.active]
    inactive_hunts = [h for h in joined_hunts if not h.active]

    context = {
        "joined_hunts": joined_hunts,
        "active_hunts": active_hunts,
        "inactive_hunts": inactive_hunts
    }
    return render(request, "hunts.html", context)


class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user_settings.html', {'chpw': PasswordChangeForm(request.user)})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'user_settings.html', {'chpw': form})
