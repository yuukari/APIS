from django.conf.urls import url

from . import views

app_name = 'frontend'

urlpatterns = [
	url(r'^$', views.index, name='index'),


	url(r'^backend/$', views.backendDash, name='backend-dash'),
]
