# jobs/admin.py

# DJANGO MODULES
from django.contrib import admin

# IMPORT CUSTOME MODELS
from jobs.models import Job

# REGISTER MODELS
admin.site.register(Job)
