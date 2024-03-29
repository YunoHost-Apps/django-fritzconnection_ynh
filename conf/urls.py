"""
    urls.py
    ~~~~~~~
"""


from django.conf import settings
from django.urls import include, path


if settings.PATH:
    # settings.PATH is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH":
    urlpatterns = [
        path(f'{settings.PATH}/', include('djfritz_project.urls')),
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from djfritz_project.urls import urlpatterns  # noqa
