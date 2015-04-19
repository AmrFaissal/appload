from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import App
from .forms import AppForm


def home(request):
	return render(request, 'main/home.html')


def new_app(request):
	if request.method == 'POST':
		form = AppForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return render_to_response('main/list.html', { 'apps_list': App.objects.all() },
							context_instance=RequestContext(request))
	else:
		form = AppForm()
		
	return render(request, 'main/new_app.html', {'form': form})


def delete(request, pk):
	app = get_object_or_404(App, pk=pk)
	app.delete()
	return render_to_response('main/list.html', { 'apps_list': App.objects.all() },
					context_instance=RequestContext(request))


def edit(request, pk):
	app = get_object_or_404(App, pk=pk)
			
	if request.method == 'POST':
		form = AppForm(request.POST, request.FILES, instance=app)
		if form.is_valid():
			form.save(commit=True)
			return render_to_response('main/list.html', { 'apps_list': App.objects.all() },
							context_instance=RequestContext(request))
	else:
		form = AppForm(instance=app)

	return render(request, 'main/edit.html', {'form': form, 'pk': app.pk})


def list(request):
	rc = RequestContext(request, {'apps_list': App.objects.all()})
	return render_to_response('main/list.html', rc)

