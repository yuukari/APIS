# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q
#from django.views.generic.edit import FormView
from registration.models import Event
from .models import Panel,Panelist,Room,PanelRequest,PanelComment,PanelSlot,Track
from .forms import PanelForm

import datetime

events = Event.objects.all()
event = Event.objects.get(name__icontains="2018")

# Create your views here.

#@login_required(login_url='/login/')
def visual(request):
	return render(request, 'visual.html', {"events": events, "event": event})

def visualHorizontal(request):
	return render(request, 'visual_horizontal.html', {"events": events, "event": event})

#@login_required(login_url='/login/')
def glance(request):
	return render(request, 'glance.html', {"events": events, "event": event})

#@login_required(login_url='/login/')
def ControlsV1GetPanels(request):
	panels = PanelSlot.objects.filter(event=event)
	output = {}
	for x in panels:
		if x.label == None or x.label == "":
			x.label = x.get_title()
		output[str(x.pk)] = {
					"pk": str(x.pk),
					"panelist": str(x.get_panelist()),
					"event": str(x.event),
					"room": str(x.room.pk),
					"title": str(x.label),
					"time_start": str(timezone.localtime(x.time_start).strftime("%a %I:%M%p %Z")),
					"time_slot": timezone.localtime(x.time_start).strftime("%m%d%H%M"),
					"date_slot": timezone.localtime(x.time_start).strftime("%m%d"),
					"block_slot": timezone.localtime(x.time_start).strftime("%H%M"),
					"setup": str((timezone.timedelta(minutes=x.setup_time).days * 24)+timezone.timedelta(minutes=x.setup_time).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.setup_time).seconds//60)%60)+" Minutes",
					"setup_small": str((timezone.timedelta(minutes=x.setup_time).days * 24)+timezone.timedelta(minutes=x.setup_time).seconds//3600)+"H "+str((timezone.timedelta(minutes=x.setup_time).seconds//60)%60)+"M",
					"setup_blocks": x.setup_time / 15,
					"duration": str((timezone.timedelta(minutes=x.duration).days * 24)+timezone.timedelta(minutes=x.duration).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.duration).seconds//60)%60)+" Minutes",
					"duration_small": str((timezone.timedelta(minutes=x.duration).days * 24)+timezone.timedelta(minutes=x.duration).seconds//3600)+"H "+str((timezone.timedelta(minutes=x.duration).seconds//60)%60)+"M",
					"duration_blocks": x.duration / 15,
					"r18": x.get_r18(),
					"track": x.get_track_name(),
					"color": x.get_track_color(),
					"click": x.get_click_action(),
					}
	return JsonResponse(output)

#@login_required(login_url='/login/')
def ControlsV1GetRooms(request):
	rooms = Room.objects.filter(event=event).order_by('pk')
	output = {}
	for x in rooms:
		output[str(x.pk)] = {
					"pk": str(x.pk),
					"name": x.name,
				}
	return JsonResponse(output)

#@login_required(login_url='/login/')
def ControlsV1GetEventDetail(request):
	output = {}

	days = (event.eventEnd - event.eventStart).days

	names = []
	names_full = []
	day_blocks = {}
	reverse_day_blocks = {}
	reverse_day_blocks_full = {}

	i = 0
	while i <= days:
		names.append( ( (event.eventStart+timezone.timedelta(days=i)).strftime("%A"), (event.eventStart+timezone.timedelta(days=i)).strftime("%m%d")  ) )
		names_full.append( ( (event.eventStart+timezone.timedelta(days=i)).strftime("%A"), (event.eventStart+timezone.timedelta(days=i)).strftime("%m%d%Y")  ) )
		day_blocks[(event.eventStart+timezone.timedelta(days=i-1)).strftime("%m%d")] = i
		reverse_day_blocks[i] = (event.eventStart+timezone.timedelta(days=i-1)).strftime("%m%d")
		reverse_day_blocks_full[i] = (event.eventStart+timezone.timedelta(days=i-1)).strftime("%m%d%Y")
		i = i + 1

	day_blocks[(event.eventStart+timezone.timedelta(days=i-1)).strftime("%m%d")] = i
	reverse_day_blocks[i] = (event.eventStart+timezone.timedelta(days=i-1)).strftime("%m%d")
	reverse_day_blocks_full[i] = (event.eventStart+timezone.timedelta(days=i-1)).strftime("%m%d")
	day_blocks[(event.eventStart+timezone.timedelta(days=i)).strftime("%m%d")] = i+1
	reverse_day_blocks[i+1] = (event.eventStart+timezone.timedelta(days=i)).strftime("%m%d")
	reverse_day_blocks_full[i+1] = (event.eventStart+timezone.timedelta(days=i)).strftime("%m%d")


	output[str(event.pk)] = {
				"title": event.name,
				"start_date": event.eventStart.strftime("%m%d"),
				"start_date_full": event.eventStart.strftime("%m%d%Y"),
				"days": days,
				"names": names,
				"names_full": names_full,
				"reverse_day_blocks": reverse_day_blocks,
				"reverse_day_blocks_full": reverse_day_blocks_full,
				"day_blocks": day_blocks,
				}
	return JsonResponse(output)


#@login_required(login_url='/login/')
def ControlsV1Blocks(request):
	blocks = {}
	blocks['blocks'] = {
1:"0700",
2:"0715",
3:"0730",
4:"0745",
5:"0800",
6:"0815",
7:"0830",
8:"0845",
9:"0900",
10:"0915",
11:"0930",
12:"0945",
13:"1000",
14:"1015",
15:"1030",
16:"1045",
17:"1100",
18:"1115",
19:"1130",
20:"1145",
21:"1200",
22:"1215",
23:"1230",
24:"1245",
25:"1300",
26:"1315",
27:"1330",
28:"1345",
29:"1400",
30:"1415",
31:"1430",
32:"1445",
33:"1500",
34:"1515",
35:"1530",
36:"1545",
37:"1600",
38:"1615",
39:"1630",
40:"1645",
41:"1700",
42:"1715",
43:"1730",
44:"1745",
45:"1800",
46:"1815",
47:"1830",
48:"1845",
49:"1900",
50:"1915",
51:"1930",
52:"1945",
53:"2000",
54:"2015",
55:"2030",
56:"2045",
57:"2100",
58:"2115",
59:"2130",
60:"2145",
61:"2200",
62:"2215",
63:"2230",
64:"2245",
65:"2300",
66:"2315",
67:"2330",
68:"2345",
69:"0000",
70:"0015",
71:"0030",
72:"0045",
73:"0100",
74:"0115",
75:"0130",
76:"0145",
77:"0200",
78:"0215",
79:"0230",
80:"0245",
81:"0300",
82:"0315",
83:"0330",
84:"0345",
85:"0400",
86:"0415",
87:"0430",
88:"0445",
89:"0500",
90:"0515",
91:"0530",
92:"0545",
93:"0600",
94:"0615",
95:"0630",
96:"0645",
}
	return JsonResponse(blocks)

#@login_required(login_url='/login/')
def ControlsV1ReverseBlocks(request):
	blocks = {}
	blocks['blocks'] = {
"0700":1,
"0715":2,
"0730":3,
"0745":4,
"0800":5,
"0815":6,
"0830":7,
"0845":8,
"0900":9,
"0915":10,
"0930":11,
"0945":12,
"1000":13,
"1015":14,
"1030":15,
"1045":16,
"1100":17,
"1115":18,
"1130":19,
"1145":20,
"1200":21,
"1215":22,
"1230":23,
"1245":24,
"1300":25,
"1315":26,
"1330":27,
"1345":28,
"1400":29,
"1415":30,
"1430":31,
"1445":32,
"1500":33,
"1515":34,
"1530":35,
"1545":36,
"1600":37,
"1615":38,
"1630":39,
"1645":40,
"1700":41,
"1715":42,
"1730":43,
"1745":44,
"1800":45,
"1815":46,
"1830":47,
"1845":48,
"1900":49,
"1915":50,
"1930":51,
"1945":52,
"2000":53,
"2015":54,
"2030":55,
"2045":56,
"2100":57,
"2115":58,
"2130":59,
"2145":60,
"2200":61,
"2215":62,
"2230":63,
"2245":64,
"2300":65,
"2315":66,
"2330":67,
"2345":68,
"0000":69,
"0015":70,
"0030":71,
"0045":72,
"0100":73,
"0115":74,
"0130":75,
"0145":76,
"0200":77,
"0215":78,
"0230":79,
"0245":80,
"0300":81,
"0315":82,
"0330":83,
"0345":84,
"0400":85,
"0415":86,
"0430":87,
"0445":88,
"0500":89,
"0515":90,
"0530":91,
"0545":92,
"0600":93,
"0615":94,
"0630":95,
"0645":96,
}
	return JsonResponse(blocks)

def testform(request):
	form = PanelForm(initial={'event': event},event=event)
	return render(request, 'testform.html', {'events': events, 'event': event, 'form': form})

def manager(request,track_id=None):
	panels = Panel.objects.filter(event=event)
	filter = ""
	if track_id != None:
		track = get_object_or_404(Track, pk=track_id)
		panels = panels.filter(track=track)
		filter=": "+track.title
	context = {
		"event": event,
		"events": events,
		"list": panels,
		"filter": filter
		}
	return render(request, 'manager.html', context)


def checkIn(request):
	panelists = Panelist.objects.filter(event=event).order_by('-fan_name')
	pnx = {}
	for x in panelists:
		pnx[str(x.pk)] = {"panelist": x,
				"panels": PanelSlot.objects.filter(event=event,panel__isnull=False).order_by('time_start')}
	context = {
		"event": event,
		"events": events,
		"list": pnx,
		}
	return render(request, 'checkin.html', context)

def panelDetail(request,panel_id):
	panel = get_object_or_404(Panel,pk=panel_id)
	slots = PanelSlot.objects.filter(panel=panel)
	requests = PanelRequest.objects.filter(panel=panel)
	comments = PanelComment.objects.filter(panel=panel).order_by('-date_added')
	context = {
		"event": event,
		"events": events,
		"panel": panel,
		"slots": slots,
		"requests": requests,
		"comments": comments,
	}	
	return render(request, 'event_detail.html', context)

def slotMod(request,slot_id=None):
	if slot_id == None:
		# new
		if request.method == "POST":
			dte = str(str(request.POST['date']) + str(request.POST['hour']) + str(request.POST['minute']))
			n = PanelSlot(
				event=event,
				label=request.POST['label'],
				setup_notes=request.POST['setup_notes'],
				time_start=datetime.datetime.strptime(dte,'%m%d%Y%H%M'),
				duration=request.POST['duration'],
				setup_time=request.POST['setup_time'],
				room=Room.objects.filter(pk=request.POST['room']).first()
			)
			if request.POST['label'] == u'':
				n.label = None
			if request.POST['setup_notes'] == u'':
				n.setup_notes = None
			if request.POST['panel'] == u'':
				n.panel = None
			else:
				n.panel = Panel.objects.filter(pk=request.POST['panel']).first()
			n.save()
			if request.POST['popup']:
				return redirect("events:helper-close")
			return redirect("events:new-slot")
		else:
			durations = PanelSlot.DURATIONS
			setup_time = PanelSlot.SETUP_TIMES
			panels = Panel.objects.filter(event=event).order_by('title')
			return render(request, 'slot_mod.html', {"slot_id": slot_id, "durations": PanelSlot.DURATIONS, "setup_time": setup_time, "panels": panels,"event": event, "slot": None})
	else:
		# previous
		slot = get_object_or_404(PanelSlot, pk=slot_id)
		if request.method == "POST":
			dte = str(str(request.POST['date']) + str(request.POST['hour']) + str(request.POST['minute']))
			time = datetime.datetime.strptime(dte,'%m%d%Y%H%M')
			slot.label=request.POST['label']
			slot.setup_notes=request.POST['setup_notes']
			slot.time_start=datetime.datetime.strptime(dte,'%m%d%Y%H%M')
			slot.duration=request.POST['duration']
			slot.setup_time=request.POST['setup_time']
			slot.room=Room.objects.filter(pk=request.POST['room']).first()
			if request.POST['label'] == u'':
				slot.label = None
			if request.POST['setup_notes'] == u'':
				slot.setup_notes = None
			if request.POST['panel'] == u'':
				slot.panel = None
			else:
				slot.panel = Panel.objects.filter(pk=request.POST['panel']).first()
			slot.save()
			if request.POST['popup']:
				return redirect("events:helper-close")
			return redirect("events:edit-slot",slot_id=slot.pk)
		else:
			durations = PanelSlot.DURATIONS
			setup_time = PanelSlot.SETUP_TIMES
			panels = Panel.objects.filter(event=event).order_by('title')
			return render(request, 'slot_mod.html', {"slot_id": slot_id, "durations": PanelSlot.DURATIONS, "setup_time": setup_time, "panels": panels,"event": event, "slot": slot})

def ControlsV1HelperClose(request):
	return render(request, 'helper_close.html', {})

def manageSlot(request,slot_id=None):
	pass


def ControlsV1CheckInPanelist(request,panelist_id):
	panelist = get_object_or_404(Panelist,pk=panelist_id)
	panelist.checked_in = True
	panelist.checked_in_date = timezone.now()
	panelist.save()
	return JsonResponse({"status": "OK"})

#@login_required(login_url='/login/')
def ControlsV1PullPanelVerification(request,panel_id):
	panel = get_object_or_404(PanelSlot,pk=panel_id)
	m_panel_time_end = timezone.localtime(panel.time_start+timezone.timedelta(minutes=panel.duration))
	m_panel_start_setup =  timezone.localtime(panel.time_start-timezone.timedelta(minutes=panel.setup_time))
	output = {
			"panel": {},
			"panel_before": {},
			"panel_after": {},
			"panels_aside": {},
			"conflicts": [],
			"adjs": [],
		}

	output['panel'] = {
				"title": panel.panel.title,
				"event": str(panel.event),
				"room": str(panel.room),
				"time_start": str(timezone.localtime(panel.time_start).strftime("%a %I:%M%p %Z")),
				"time_end": str(timezone.localtime(panel.time_start+timezone.timedelta(minutes=panel.duration)).strftime("%a %I:%M%p %Z")),
			}

	lai = []

	# 1. what panels are beside this onw
	# 2. What's coming next
	# 3. What just happened
	# 4. Is there any conflicts?

	rooms = {}


	for y in Room.objects.filter(event=event):
		rooms[y.pk] = []
		#asidei = 0
		beforei = 0
		for x in PanelSlot.objects.filter(Q(event=event) and Q(room=y)).order_by('time_start'):
			checked = 0
			# (datecode, meta, model)
			# meta
			# [0/1]
			rooms[y.pk].append(x)

			#asidei = asidei - 1
			beforei = beforei - 1

			# checking for before/after. Check if panel is =, then take the immediate last one

			if x == panel:
				beforei = 1
				panel_before = rooms[y.pk][len(rooms[y.pk])-2]
				time_end = timezone.localtime(panel_before.time_start+timezone.timedelta(minutes=panel_before.duration))
				time_start_setup = timezone.localtime(panel_before.time_start-timezone.timedelta(minutes=panel_before.setup_time))
				try:
					if panel_before == panel:
						output['panel_before'] = {}
					else:
						output['panel_before'] = {
										"title": panel_before.get_title(),
										"event": str(panel_before.event),
										"room": str(panel_before.room),
										"time_start": str(timezone.localtime(panel_before.time_start).strftime("%a %I:%M%p %Z")),
										"time_end": str(timezone.localtime(panel_before.time_start+timezone.timedelta(minutes=panel_before.duration)).strftime("%a %I:%M%p %Z")),
										"panelist": str(panel_before.get_panelist()),
										"panelist_pk": str(panel_before.get_panelist_pk()),
									}

									
				except:
					output['panel_before'] = None
				# check timing conflicts
				# 1. check if start is during before

				if panel.time_start > time_start_setup and panel.time_start < time_end and panel != x:
					output['conflicts'].append("Panel starts during Previous Panel ("+str(panel_before)+")")

				# 2. check if setup start is during before
				if m_panel_start_setup > time_start_setup and m_panel_start_setup < time_end and panel != x:
					output['conflicts'].append("Panel Setup time starts during Previous Panel ("+str(panel_before)+")")

			if beforei == 0:
				panel_after = x
				time_end = timezone.localtime(panel_after.time_start+timezone.timedelta(minutes=panel_after.duration))
				time_start_setup = timezone.localtime(panel_after.time_start-timezone.timedelta(minutes=panel_after.setup_time))
				try:
					output['panel_after'] = {
									"title": str(panel_after),
									"event": str(panel_after.event),
									"room": str(panel_after.room),
									"time_start": str(timezone.localtime(panel_after.time_start).strftime("%a %I:%M%p %Z")),
									"time_end": str(timezone.localtime(panel_after.time_start+timezone.timedelta(minutes=panel_after.duration)).strftime("%a %I:%M%p %Z")),
									"panelist": str(panel_after.get_panelist()),
									"panelist_pk": str(panel_after.get_panelist_pk()),
								}

									
				except:
					output['panel_after'] = None

				# check timing conflicts
				# 1. check if start is during after
				if panel.time_start > time_start_setup and panel.time_start < time_end:
					output['conflicts'].append("Panel starts during Following Panel ("+str(panel_after)+")")

				# 2. check if setup start is during after
				if m_panel_start_setup > time_start_setup and m_panel_start_setup < time_end:
					output['conflicts'].append("Panel Setup time starts during Following Panel ("+str(panel_after)+")")

				# 3. check if end is anywhere beyond the time start of after
				if m_panel_time_end > time_start_setup:
					output['conflicts'].append("Panel Ends During or After Following Panel ("+str(panel_after)+")")

			time_start_setup = timezone.localtime(x.time_start-timezone.timedelta(minutes=x.setup_time))
			time_end = timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration))

			if panel.time_start >= time_start_setup and panel.time_start <= time_end and checked == 0:
				checked = 1
				if x.room != panel.room:
					output['adjs'].append({
							"title": str(x),
							"event": str(x.event),
							"room": str(x.room),
							"panelist": str(x.get_panelist()),
							"panelist_pk": str(x.get_panelist_pk()),
							"room_pk": str(x.room.pk),
							"time_start": str(timezone.localtime(x.time_start).strftime("%a %I:%M%p %Z")),
							"time_end": str(timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration)).strftime("%a %I:%M%p %Z")),
							"track": x.get_track_name(),
							"color": x.get_track_color(),
						})

			if m_panel_time_end >= time_start_setup and m_panel_time_end <= time_end and checked == 0:
				checked = 1
				if x.room != panel.room:
					output['adjs'].append({
							"title": str(x),
							"event": str(x.event),
							"room": str(x.room),
							"room_pk": str(x.room.pk),
							"panelist": str(x.get_panelist()),
							"panelist_pk": str(x.get_panelist_pk()),
							"time_start": str(timezone.localtime(x.time_start).strftime("%a %I:%M%p %Z")),
							"time_end": str(timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration)).strftime("%a %I:%M%p %Z")),
							"track": x.get_track_name(),
							"color": x.get_track_color(),
						})

#			output = {
#					"pk": str(x.pk),
#					"panelist": str(x.panelist),
#					"event": str(x.event),
#					"room": str(x.room.pk),
#					"title": str(x.title),
#					"time_start": timezone.localtime(x.time_start),
#					"time_end": timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration),
#					"time_slot": timezone.localtime(x.time_start).strftime("%m%d%H%M"),
#					"setup": str(timezone.timedelta(minutes=x.setup_time).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.setup_time).seconds//60)%60)+" Minutes",
#					"duration": str(timezone.timedelta(minutes=x.duration).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.duration).seconds//60)%60)+" Minutes",
#					"r18": x.r18,
#					"type": x.type,
#				}
	return JsonResponse(output)
#@login_required(login_url='/login/')
def ControlsV1PullEvents(request):
	#now = timezone.localtime(timezone.make_aware(datetime.datetime.strptime('08/24/2017 17:56', '%m/%d/%Y %H:%M')))
	now = timezone.localtime(timezone.now())
	output = {}
	# Am I in the middle of an event?
	# What's the next event?
	datecode = timezone.localtime(now).strftime("%m%d%H%M")
	for y in Room.objects.filter(event=event):
		genui = []
		genui.append( (datecode, True, str(timezone.localtime(now).strftime("%a %I:%M%p %Z")), y.pk ) )
		for x in PanelSlot.objects.filter(event=event,room=y):
			# (datecode, meta, model)
			# meta
			# [0/1]

			happens = False
			in_setup = False

			if now >= timezone.localtime(x.time_start - timezone.timedelta(minutes=x.setup_time)) and now <= timezone.localtime(x.time_start):
				in_setup = True
				happens = True

			if now >= timezone.localtime(x.time_start) and now <= timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration)):
				happens = True

			outp = {
					"pk": str(x.pk),
					"panelist": str(x.get_panelist()),
					"event": str(x.event),
					"room": str(x.room.pk),
					"title": str(x.get_title()),
					"time_start": str(timezone.localtime(x.time_start).strftime("%a %I:%M%p %Z")),
					"time_end": str(timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration)).strftime("%a %I:%M%p %Z")),
					"time_slot": timezone.localtime(x.time_start).strftime("%m%d%H%M"),
					"setup": str(timezone.timedelta(minutes=x.setup_time).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.setup_time).seconds//60)%60)+" Minutes",
					"duration": str(timezone.timedelta(minutes=x.duration).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.duration).seconds//60)%60)+" Minutes",
					"r18": x.get_r18(),
					"track": x.get_track_name(),
					"color": x.get_track_color(),
					"click": x.get_click_action(),
					"happens": happens,
					"in_setup": in_setup,
				}

			genui.append( (timezone.localtime(x.time_start).strftime("%m%d%H%M"), False, outp, y.pk) )
		g2 = sorted(genui, key=lambda genui: genui[0])
		output[y.name] = g2
	return JsonResponse(output)

def ControlsV1PullEventsTimecode(request,timecode):
	now = timezone.localtime(timezone.make_aware(datetime.datetime.strptime(timecode, '%m%d%Y%H%M')))
	#now = timezone.localtime(timezone.now())
	output = {}
	# Am I in the middle of an event?
	# What's the next event?
	datecode = timezone.localtime(now).strftime("%m%d%H%M")
	for y in Room.objects.filter(event=event):
		genui = []
		genui.append( (datecode, True, str(timezone.localtime(now).strftime("%a %I:%M%p %Z")), y.pk ) )
		for x in PanelSlot.objects.filter(event=event,room=y):
			# (datecode, meta, model)
			# meta
			# [0/1]

			happens = False
			in_setup = False

			if now >= timezone.localtime(x.time_start - timezone.timedelta(minutes=x.setup_time)) and now <= timezone.localtime(x.time_start):
				in_setup = True
				happens = True

			if now >= timezone.localtime(x.time_start) and now <= timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration)):
				happens = True

			outp = {
					"pk": str(x.pk),
					"panelist": str(x.get_panelist()),
					"event": str(x.event),
					"room": str(x.room.pk),
					"title": str(x.get_title()),
					"time_start": str(timezone.localtime(x.time_start).strftime("%a %I:%M%p %Z")),
					"time_end": str(timezone.localtime(x.time_start+timezone.timedelta(minutes=x.duration)).strftime("%a %I:%M%p %Z")),
					"time_slot": timezone.localtime(x.time_start).strftime("%m%d%H%M"),
					"setup": str(timezone.timedelta(minutes=x.setup_time).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.setup_time).seconds//60)%60)+" Minutes",
					"duration": str(timezone.timedelta(minutes=x.duration).seconds//3600)+" Hours, "+str((timezone.timedelta(minutes=x.duration).seconds//60)%60)+" Minutes",
					"r18": x.get_r18(),
					"happens": happens,
					"in_setup": in_setup,
					"track": x.get_track_name(),
					"color": x.get_track_color(),
					"click": x.get_click_action(),
				}

			genui.append( (timezone.localtime(x.time_start).strftime("%m%d%H%M"), False, outp, y.pk) )
		g2 = sorted(genui, key=lambda genui: genui[0])
		output[y.name] = g2
	return JsonResponse(output)


