from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^addPage$', views.addPage),
    url(r'^addApp$', views.addApp),
    url(r'^appointments$', views.appointments),
    url(r'^delete(?P<id>\d+)$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
]