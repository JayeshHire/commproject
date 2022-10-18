from django.urls import include , re_path
from . import  views

urlpattern = [
    re_path(r'^createUser/$',views.create,name ='create'), #this routes to page for creating user
    re_path(r'^login/$', views.login, name ="login"),#route  to user login
    re_path(r'post_content', views.content ,name = 'content'),#routes to user interface for posting content
]
