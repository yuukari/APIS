# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from registration.models import Event

event = Event.objects.get(name__icontains="2018")

def checkStaff(request):
	if request.user.is_staff:
		return True
	else:
		return render(request, 'not_allowed.html', {"event": event})

# Create your views here.
def index(request):
	return render(request, 'frontend_index.html', {"event": event})

def backendDash(request):
	if checkStaff(request):
		context = {
			"event": event,
			}
		return render(request, 'backend_index.html', context)
