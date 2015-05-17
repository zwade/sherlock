from django.conf.urls import url, include
from .views import app
from .views import auth
from .views import game

huntpatterns = [
    url(r'^$', game.HuntView.as_view(), name='view_hunt'),
    url(r'^slideshow$', game.Slideshow.as_view(), name='view_hunt_slideshow'),
    url(r'^join$', game.JoinHunt.as_view(), name='join_hunt'),
    url(r'^edit$', game.EditHuntView.as_view(), name='edit_hunt'),
    url(r'^clues/new$', game.NewClueAjax.as_view(), name='add_clue'),
    url(r'^clues/delete$', game.DeleteClueAjax.as_view(), name='delete_clue'),
    url(r'^clues$', game.CluesView.as_view(), name='view_clues'),
    url(r'^submit$', game.SubmissionAjax.as_view(), name='submit_image'),
]

urlpatterns = [
    url(r"^$", app.index_view, name="index"),
    url(r"^login$", auth.LoginView.as_view(), name="login"),
    url(r"^logout$", auth.logout_view, name='logout'),
    url(r"^register$", auth.RegisterView.as_view(), name='register'),
    url(r'^settings$', app.SettingsView.as_view(), name='user_settings'),
    url(r'^hunts/new$', game.NewHuntView.as_view(), name='new_hunt'),
    url(r'^hunts/(?P<slug>\w{8,})/', include(huntpatterns)),
    url(r'^h/(?P<slug>\w{8,})$', game.HuntView.as_view(), name='view_hunt_short'),
]
