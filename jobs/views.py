# jobs/views.py

# DJANGO MODULES
from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# IMPORT MODELS
from jobs.models import Job, Category

# # HomeView using TemplateView
# class HomeView(TemplateView):
# 	template_name = 'jobs/index.html'

# HomeView using ListView
class HomeView(ListView):
	'''use Job model'''
	model = Job 
	'''use context to store objects in a variable called jobs'''
	context_object_name = 'jobs'
	'''template name to use to render the job objects'''
	template_name = 'jobs/index.html'
	'''add pagination by using paginate_by function'''
	paginate_by = 1

	'''define contex data for Category'''
	def get_context_data(self, **kwargs):
		contex = super(HomeView, self).get_context_data(**kwargs)
		contex['categories'] = Category.objects.all()
		return contex
