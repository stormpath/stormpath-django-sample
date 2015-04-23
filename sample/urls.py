from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView, RedirectView
import django_stormpath

from .views import *


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^django-register/$', register, name='register'),
    url(r'^django-logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
    url(r'^django-login/$', stormpath_login, name='login'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
)

