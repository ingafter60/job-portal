# users/urls.py

# IMPORT DJANGO MODULES
from django.urls import path

# IMPORT FUNCTIONS
from .views import *

# DEFINING APP ATTRIBUTE
app_name = 'users'

# DEFINING URL PATH
urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register')
]

