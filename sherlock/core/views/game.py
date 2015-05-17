from django import http
from django.shortcuts import render, redirect
from django.views.generic import View
from ..models import Hunt, Clue, Submission
from ..forms.game import SubmissionForm, HuntForm, ClueForm
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

        return render(request, 'edit_hunt.html', {'edit': HuntForm(hunt), 'clue': ClueForm(), 'hunt': hunt, 'clues': hunt.clues.all()})


class NewClueAjax(LoginRequiredMixin, View):
    def post(self, request, slug):
        form = ClueForm(request.POST)

        if form.is_valid():
            clue = form.save(commit=False)
            clue.hunt = Hunt.objects.get(slug=slug)
            clue.save()

            return render(request, 'clue_row.html', {'clue': clue})

        raise render(request, 'clue_form.html', {'clue': form}, status=400)


class HuntView(View):
    def get(self, request, slug):
        if request.resolver_match.url_name != 'view_hunt':
            return redirect('view_hunt', slug=slug, permanent=True)

        hunt = Hunt.objects.get(slug=slug)
        
        if hunt.owner == request.user:
            return render(request, 'edit_hunt.html', {"form": hunt})

        return render(request, 'hunt.html', {
            'hunt': hunt,
            'owned': hunt.owner == request.user,
            'joined': request.user.joined_hunts.filter(slug=slug).exists()
        })


class CluesView(LoginRequiredMixin, View):
    def get(self, request, slug):
        if not request.user.joined_hunts.filter(slug=slug).exists():
            return redirect('view_hunt', slug=slug)

        hunt = Hunt.objects.get(slug=slug)
        clues = dict((x.id, x) for x in Clue.objects.filter(hunt__slug=slug))

        for submission in Submission.objects.filter(clue__in=clues, user=request.user):
            if submission.valid:
                clues[submission.clue.id].solved = True

        return render(request, 'clues.html', {'clues': clues.values(), 'hunt': hunt, 'form': SubmissionForm()})


class SubmissionAjax(LoginRequiredMixin, View):
    def post(self, request, slug):
        form = SubmissionForm(request.POST)

        if form.is_valid():
            submission = form.save(commit=False)
            submission.clue = Clue.objects.get(id=form.cleaned_data['clue'])
            submission.save()

            return http.HttpResponse()

        return HttpResponse(status=400)

class JoinHunt(LoginRequiredMixin, View):
    def post(self, request, slug):
        hunt = Hunt.objects.get(slug=slug)

        hunt.participants.add(request.user)
        hunt.save()

        return redirect('view_clues', slug=slug)
