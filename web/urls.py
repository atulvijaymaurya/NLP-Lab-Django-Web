from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^people$',views.people, name='people'),
    url(r'^publications$',views.publications, name='publications'),
    url(r'^contactus$',views.contactus, name='contactus'),
    url(r'^gallery$',views.gallery, name='gallery'),
    url(r'^projects$',views.projects, name='gallery'),
    #url(r'^demos$',views.demos, name='gallery'),
    url(r'^',views.notfound, name='notfound')
];