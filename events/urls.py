from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
	url(r'^panels/testform/$', views.testform, name='testform'),
	url(r'^manage/checkin/$', views.checkIn, name='checkin'),
	url(r'^manage/manager/$', views.manager, name='manager'),
	url(r'^manage/manager/track/(?P<track_id>[\w-]+)/$', views.manager, name='manager-track'),
	url(r'^manage/panel/(?P<panel_id>[\w-]+)/$', views.panelDetail, name='panel-detail'),
	url(r'^manage/visual/$', views.visual, name='visual'),
	url(r'^manage/glance/$', views.glance, name='glance'),	
	url(r'^controls/v1/pull/events/$', views.ControlsV1PullEvents, name='ControlsV1PullEvents'),
	url(r'^controls/v1/pull/events/(?P<timecode>[\w-]+)/$', views.ControlsV1PullEventsTimecode, name='ControlsV1PullEventsTimecode'),
	url(r'^controls/v1/$', views.ControlsV1GetEventDetail, name='ControlsV1GetEventDetail'),
	url(r'^controls/v1/panelist/(?P<panelist_id>[\w-]+)/checkin/$', views.ControlsV1CheckInPanelist, name='ControlsV1CheckInPanelist'),
	url(r'^controls/v1/panel/(?P<panel_id>[\w-]+)/verification/$', views.ControlsV1PullPanelVerification, name='ControlsV1PullPanelVerification'),	
	url(r'^controls/v1/panels/$', views.ControlsV1GetPanels, name='ControlsV1GetPanels'),	
	url(r'^controls/v1/rooms/$', views.ControlsV1GetRooms, name='ControlsV1GetRooms'),
	url(r'^controls/v1/helpers/blocks/$', views.ControlsV1Blocks, name='blocks'),
	url(r'^controls/v1/helpers/reverseblocks/$', views.ControlsV1ReverseBlocks, name='reverseblocks'),
]
