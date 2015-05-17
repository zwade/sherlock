from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from ..forms import AuthenticationForm, UserCreationForm


class login_view(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/')
        return render(request, 'login.html', {'form': AuthenticationForm()})

    def post(self, request):
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.GET.get('next', '/')

            return redirect(next_url)

        return render(request, 'login.html', {'form': form})


class register_view(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/')
        return render(request, 'register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # Login the created user

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data('password'))
            login(request, user)

            return redirect('/')

        return render(request, 'register.html', {form: form})


def index_view(request):
    if not request.user.is_authenticated():
        return render(request, 'index.html')
    return render(request, 'hunts.html')
