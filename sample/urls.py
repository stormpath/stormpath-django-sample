from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from .views import *


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^django-register/$', register, name='register'),
    url(r'^django-login/$', stormpath_login, name='login'),
    url(r'^django-logout/$', stormpath_logout, name='logout'),
)
