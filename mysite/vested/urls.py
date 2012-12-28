from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^register/', 'vested.views.register', name='register'),
    url(r'^register_action/', 'vested.views.register_action', name='register_action'),
    url(r'^login/', 'vested.views.login', name='login'),
    url(r'^login_action/', 'vested.views.login_action', name='login_action'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
