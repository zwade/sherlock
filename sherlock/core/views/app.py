import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .auth import LoginView

logger = logging.getLogger(__name__)


def index_view(request):
    if not request.user.is_authenticated():
        return render(request, "splash.html")
    return render(request, "hunts.html")
