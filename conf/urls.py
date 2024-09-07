"""
    urls.py
    ~~~~~~~
"""


from django.conf import settings
from django.urls import include, path
from django.views.generic import RedirectView


if settings.PATH_URL:
    # settings.PATH_URL is __PATH__
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path('', RedirectView.as_view(url=f'{settings.PATH_URL}/')),
        path(f'{settings.PATH_URL}/', include('djfritz_project.urls')),
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from djfritz_project.urls import urlpatterns  # noqa
