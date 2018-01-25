from django.conf.urls import url

from . import views

app_name = 'frontend'

urlpatterns = [
	url(r'^$', views.index, name='index'),


	url(r'^backend/$', views.backendDash, name='backend-dash'),
	url(r'^backend/hr/$', views.backendHR, name='backend-hr-dash'),
	url(r'^backend/hr/roster/$', views.staffRoster, name='backend-hr-roster'),
	url(r'^backend/hr/roster/(?P<dept_pk>[\w-]+)/$', views.staffRoster, name='backend-hr-roster-department'),
]
