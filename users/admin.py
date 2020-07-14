# users/admin.py

# IMPORT DEFAULT DJANGO MODULES
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# IMPORT MODELS FROM USERS APP
from users.models import Account

# CREATE CLASS TO MANAGE LIST OF USERS AND FILTER USERS IN ADMIN PANEL
class MyAdminAccounts(UserAdmin):

	'''Use the Account model'''
	model = Account
	'''creating table fields in admin to list the users'''
	list_display = ('email', 'first_name', 'last_name', 'is_employee', 'is_employer')
	'''creating table fields in admin to filter the users'''
	list_filter = ('email', 'first_name', 'last_name', 'is_employee', 'is_employer')
	'''creating search field'''
	search_fields = ('email', 'first_name', 'last_name')
	'''ordering email and fistname'''
	ordering = ('email', 'first_name')
	'''read only field - MUST be a list or tuple'''
	readonly_fields = ['date_joined'] # <-- this tuple & this list --> ('date_joined',)

	# Add A New User
	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields':('email', 'first_name', 'last_name', 'password1', 'password2', 'is_employee', 'is_employer', 'is_active')
		}),
	)

	# # Update User
	fieldsets = (
		(None, {'fields':('email', 'first_name', 'last_name', 'password')}),
		('Permissions', {'fields':('is_staff', 'is_active', 'is_employee', 'is_employer')})
	)

# REGISTER MODELS AND NEW CLASS TO ADMIN
admin.site.register(Account, MyAdminAccounts)	