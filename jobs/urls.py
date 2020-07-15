# jobs/urls.py

# IMPORT DJANGO MODULES
from django.urls import path

# IMPORT FUNCTIONS
from .views import *

# DEFINING APP ATTRIBUTE
app_name = 'jobs'

# DEFINING PATH
urlpatterns = [
	path('', HomeView.as_view(), name='home')
]