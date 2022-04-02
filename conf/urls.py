from django.conf import settings
from django.conf.urls import static
from django.urls import include, path


# from django_yunohost_integration.views import request_media_debug_view


if settings.PATH_URL:
    # settings.PATH_URL is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        # path(f'{settings.PATH_URL}/debug/', request_media_debug_view),

        path(f'{settings.PATH_URL}/', include('djfritz_project.urls')),
    ]
    if settings.SERVE_FILES:
        urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from djfritz_project.urls import urlpatterns  # noqa
