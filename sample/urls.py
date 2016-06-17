from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView, RedirectView
import django_stormpath

from .views import *


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^django-register/$', register, name='register'),
    url(r'^django-login/$', stormpath_login, name='login'),
    url(r'^django-logout/$', stormpath_logout, name='logout'),
    url(r'^stormpath-id-site-callback/$', handled_stormpath_id_site_callback,
        name='stormpath_id_site_callback'),
)

if settings.USE_ID_SITE:
    urlpatterns += patterns('',
        url(r'', include(django_stormpath.urls)),
    )
