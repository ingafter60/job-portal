# users/views.py

# DJANGO MODULES
from django.shortcuts import render
from django.views.generic import TemplateView

# DIFINING VIEWS HERE
class UserRegisterView(TemplateView):
	template_name = 'users/user-register.html'
