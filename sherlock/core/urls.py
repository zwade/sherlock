from django.conf.urls import url
from .views import app
from .views import auth

urlpatterns = [
    url(r"^$", auth.index_view),
    url(r"^login$", auth.login_view),
    url(r"^logout$", auth.logout_view),
    url(r"^register$", auth.register_view),
]
