from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += patterns(
    'main.views',
    url(r'^$', 'home'),
    url(r'^list$', 'list'),
    url(r'app/new/$', 'new_app'),
    url(r'app/edit/(?P<pk>[0-9]+)/$', 'edit'),
    url(r'app/delete/(?P<pk>[0-9]+)/$', 'delete')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

