from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from .core import urls as core_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]


urlpatterns += [url(r"^", include(core_urls))]
