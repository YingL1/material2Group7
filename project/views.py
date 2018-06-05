# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import RegisterForm, DeviceForm
from .models import DeviceModel, Device,Component
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
	redirect_to = request.POST.get('next', request.GET.get('next', ''))
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegisterForm()
	return render(request, 'register.html', context={'form': form})

def index(request):
    return render(request, 'index.html')


def profile(request):
	user = request.user
	form_sumbit = False
	if request.method == 'POST':
		form = DeviceForm()
		device_model = request.POST.get('device_model')
		component_working = request.POST.getlist('component_working')
		component_not_working = request.POST.getlist('component_not_working')
		form_sumbit = True
		device_model_object = DeviceModel.objects.get(pk=device_model)
		tokens = len(component_working)
		solutions = []
		tokens = len(component_working)
		for pk in component_not_working:
			componenet_object = Component.objects.get(pk=pk)
			if componenet_object.name == 'screen':
				solutions.append('replace a scress')
			if componenet_object.name == 'Battery':
				solutions.append('replace a Battery')
		return render(request, 'profile.html', context={'form': form, 'form_sumbit':form_sumbit,'tokens':tokens,'solutions':solutions})
	else:
		form = DeviceForm()
	return render(request, 'profile.html', context={'form': form,'form_sumbit':form_sumbit})
