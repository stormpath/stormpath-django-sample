from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

import django_stormpath.urls

urlpatterns = patterns('',
    url(r'', include('sample.urls', namespace='sample')),
    url(r'^admin/', include(admin.site.urls)),
)
