from django.conf.urls.defaults import *
import settings

import django_git

urlpatterns = patterns('',
    (r'^', include("django-git-tester.django_git.urls")),
)

if settings.SERVE_MEDIA:
    media_url_regex = r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:]
    urlpatterns += patterns('',
        url(media_url_regex,         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
    )
