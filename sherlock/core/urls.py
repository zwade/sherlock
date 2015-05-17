from django.conf.urls import url
from .views import app
from .views import auth

urlpatterns = [
    url(r"^$", app.index_view, name="index"),
    url(r"^login$", auth.LoginView.as_view()),
    url(r"^logout$", auth.logout_view),
    url(r"^register$", auth.RegisterView.as_view()),
]
