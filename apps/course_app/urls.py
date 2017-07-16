from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),    
    url(r'^add$', views.add),    
    url(r'^destroy/(?P<course_id>\d+)$', views.warning),    
    url(r'^delete/(?P<course_id>\d+)$', views.delete),    
    url(r'^comments/(?P<course_id>\d+)$', views.comments),    
    url(r'^(?P<course_id>\d+)/post$', views.post),    
]