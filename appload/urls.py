from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home'),
    url(r'^list$', 'main.views.list'),
    url(r'app/new/$', 'main.views.new_app', name='new_app'),
    url(r'app/edit/(?P<pk>[0-9]+)/$', 'main.views.edit', name="edit"),
    url(r'app/delete/(?P<pk>[0-9]+)/$', 'main.views.delete', name="delete")
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

