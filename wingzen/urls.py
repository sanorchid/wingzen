from django.conf.urls import patterns, include, url
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wingzen.views.index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^curriculum/', include('curriculum.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    #url(r'^msgboard/', include('msgboard.urls')),
    url(r'^news/', include('zenews.urls')),
) + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()