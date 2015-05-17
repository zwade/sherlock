from django.conf.urls import url, include
from .views import app
from .views import auth
from .views import game

huntpatterns = [
    url(r'^$', game.HuntView.as_view(), name='view_hunt'),
    url(r'^edit$', game.EditHuntView.as_view(), name='edit_hunt'),
    url(r'^clues/new$', game.NewClueAjax.as_view(), name='add_clue'),
]

urlpatterns = [
    url(r"^$", app.index_view, name="index"),
    url(r"^login$", auth.LoginView.as_view(), name="login"),
    url(r"^logout$", auth.logout_view),
    url(r"^register$", auth.RegisterView.as_view()),
    url(r'^hunts/new$', game.NewHuntView.as_view()),
    url(r'^hunts/(?P<slug>[A-Za-z]{8,})', include(huntpatterns)),
    url(r'^h/(?P<slug>[A-Za-z]{8,})$', game.HuntView.as_view(), name='view_hunt_short'),
]
