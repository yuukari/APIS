# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from registration.models import Event,Department,Staff

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

def backendHR(request):
	if checkStaff(request):
		departments = Department.objects.all()
		context = {
			"departments": departments,
			"event": event,
		}
		return render(request, 'hr_index.html', context)

def staffRoster(request,dept_pk=None):
	if checkStaff(request):
		if dept_pk == None:
			# all staff
			department = None
			staff = Staff.objects.filter(event=event).order_by('department')
		else:
			department = get_object_or_404(Department,pk=dept_pk)
			staff = department.staff().filter(event=event)
		context = {
			"event": event,
			"department": department,
			"staff": staff
		}
		return render(request, 'hr_staff_list.html', context)
