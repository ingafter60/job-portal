# users/models.py

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# CREATE USER MANAGER
class UserManager(BaseUserManager):
	pass

# CREATE MODEL ACCOUNT
class Account(AbstractBaseUser, PermissionsMixin):

	'''using email instead of username for register'''	
	email = models.EmailField(_('email address'), unique=True)
	'''self explained'''
	first_name = models.CharField(_('first name', max_length=50, black=False))
	'''self explained'''
	last_name = models.CharField(_('last name', max_length=50, black=False))
	'''date join will be automatically added'''
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	'''a new user needs to be activate before it can login'''
	is_active = models.BooleanField(_('is_staff'), default=False)
	'''to verify if a new user to be an employee'''
	is_employee = models.BooleanField(default=False)
	'''to verify if a new user to be an employer'''
	is_employer = models.BooleanField(default=False)

	objects = UserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		vervose_name = _('user')
		vervose_name_plural = _('users')
