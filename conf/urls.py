from django.conf import settings
from django.urls import include, path


if settings.PATH_URL:
    # settings.PATH_URL is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path(f'{settings.PATH_URL}/', include('djfritz_project.urls')),
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from djfritz_project.urls import urlpatterns  # noqa
