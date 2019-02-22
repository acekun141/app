from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url('post/', views.post_view, name='post'),
    url('signin/', views.signin_view, name='signin'),
    url('signup/', views.signup_view, name='signup'),
    url('logout/', views.logout_view, name="logout"),
    url('infoform/', views.infoform, name='infoform'),
    url('listpost/', views.listpost, name="listpost"),
    url('newfeed/', views.newfeed, name="newfeed"),
    url(r'^post(?P<id>[0-9]+)/$', views.post, name='singlepost'),
]