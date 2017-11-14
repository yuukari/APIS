# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from registration.models import Event

event = Event.objects.get(name__icontains="2018")

# Create your views here.
def index(request):
	return render(request, 'frontend_index.html', {"event": event})
