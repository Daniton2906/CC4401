from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details'),
    url(r'^add/', views.add, name='add'),
    url(r'^removeTodo/(?P<id>\w{0,50})/', views.removeTodo, name='removeTodo'),
    url(r'^setUpTodo/(?P<id>\w{0,50})/', views.setUpTodo, name='setUpTodo'),
    url(r'^setDownTodo/(?P<id>\w{0,50})/', views.setDownTodo, name='setDownTodo')
]
