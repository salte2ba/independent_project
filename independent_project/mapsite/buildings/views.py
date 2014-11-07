from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from buildings.models import Add_person

class mainView(generic.ListView):
	model = Add_person
	template_name = 'buildings/main.html'

class pearceView(generic.ListView):
	model = Add_person
	template_name = 'buildings/pearce.html'	
