from django.shortcuts import render, redirect
from django.views.generic import View
from ..models import Hunt
from ..forms.game import SubmissionForm, HuntForm, NewClueForm
from . import LoginRequiredMixin

class NewHuntView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'new_hunt.html', {'form': HuntForm()})

    def post(self, request):
        form = HuntForm(request.POST)

        if form.is_valid():
            newHunt = form.save(commit=False)
            newHunt.owner = request.user
            newHunt.save()

            return redirect('edit_hunt', slug=newHunt.slug)

        return render(request, 'new_hunt.html', {'form': form})

class EditHuntView(LoginRequiredMixin, View):
    def get(self, request, slug):
        return self.renderEdit(request, slug=slug)

    def post(self, request, slug):
        form = HuntForm(request.POST)

        if form.is_valid():
            return self.renderEdit(request, hunt=form.save())

        return self.renderEdit(request, slug=slug)

    def renderEdit(self, request, slug=None, hunt=None):
        if not hunt:
            hunt = Hunt.objects.get(slug=slug)

        if hunt.owner != request.user:
            return redirect('view_hunt', slug=slug)

        return render(request, 'edit_hunt.html', {'edit': HuntForm(hunt), 'clue': NewClueForm(), 'hunt': hunt, 'clues': hunt.clue_set.all()})

class NewClueAjax(LoginRequiredMixin, View):
    def post(self, request, slug):
        form = NewClueForm(request.POST)

        if form.is_valid():
            clue = form.save()

            return render(request, 'clue_row.html', {'clue': clue})

        raise render(request, 'clue_form.html', {'clue': form}, status=400)

class HuntView(View):
    def get(self, request, slug):
        hunt = Hunt.objects.get(slug=slug)

        return render(request, 'clues.html', {'hunt': hunt, 'owned': hunt.owner == request.user})
