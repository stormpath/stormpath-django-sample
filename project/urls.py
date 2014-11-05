from django.conf.urls import patterns, url, include
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'chirper.views.home', name='home'),
    url(r'^login/$', 'chirper.views.stormpath_login', name='login'),
    url(r'^logout/$', 'chirper.views.stormpath_logout', name='logout'),
    url(r'^signup/$', 'chirper.views.signup', name='signup'),
    url(r'^password/send/$', 'chirper.views.send_password_token',
        name='password_send'),
    url(r'^password/reset', 'chirper.views.reset_password',
        name='password_reset'),
    url(r'^profile/$', 'chirper.views.update_user', name='profile'),
    url(r'^chirps/delete/(\d+)/$', 'chirper.views.delete_chirp',
        name='chirp_delete'),
    url(r'^chirps/$', 'chirper.views.chirping', name='chirps'),


    url(r'^admin/', include(admin.site.urls)),
)
