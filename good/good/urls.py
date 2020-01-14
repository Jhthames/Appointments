from django.conf.urls import url,  include   
urlpatterns = [
    url(r'^', include('apps.good_app.urls')), 
]
