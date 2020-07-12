# jobs/views.py

from django.shortcuts import render

# Create your views here.

def Home(request):

	return render(request, 'jobs/home.html')