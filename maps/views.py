from django.shortcuts import render

def home(request):
	return render(request, 'maps/home.html', {})

def resources(request):
	return render(request, 'maps/resources.html', {})

def contact(request):
	return render(request, 'maps/contact.html', {})

def about(request):
	return render(request, 'maps/about.html', {})

def download(request):
	return render(request, 'maps/download.html', {})