# users/models.py

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# CREATE USER MANAGER
class UserManager(BaseUserManager):
	
	'''use this guy in migrations'''
	use_in_migrations = True

	# DEFINING USER EITHER AS EMPLOYEE OR EMPLOYER 
	'''defining that user must have email, password, and extra fileds'''
	def _create_user(self, email, password, **extra_fields):
		'''if email is not correct'''
		if not email:
			raise ValueError('Your email is not correct!')

		'''if email is correct'''
		email = self.normalize_email(email)
		'''its now, the user is using email instead of username'''
		user = self.model(email=email, **extra_fields)
		'''set password for user'''
		user.set_password(password)
		'''save user to current database'''
		user.save(using=self._db)
		return user 

	# CREATING USER EITHER AS EMPLOYEE OR EMPLOYER 
	'''password=None due to all users has password as defined above '''
	def create_user(self, email, password=None, **extra_fields): 
		'''the user is not supper user'''
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)			

	# CREATING SUPER USER
	def create_superuser(self, email, password, **extra_fields):
		'''the user is supper user'''
		extra_fields.setdefault('is_superuser', True)
		'''the user is not supper user'''
		if extra_fields.get('is_superuser') is not True:
			'''disply error message'''
			raise ValueError('Superuser must have is_superuser = True')

		return self._create_user(email, password, **extra_fields)

	# NOTE
	'''
		1. We will not use the default django user
		2. Drop the database
		3. Delete all db in migrations files before making migrations
		4. Create again the same database
	''' 
			

# CREATE ACCOUNT MODEL 
class Account(AbstractBaseUser, PermissionsMixin):

	'''using email instead of username for register'''	
	email = models.EmailField(_('email address'), unique=True)
	'''self explained'''
	first_name = models.CharField(_('first name'), max_length=50, blank=False)
	'''self explained'''
	last_name = models.CharField(_('last name'), max_length=50, blank=False)
	'''date join will be automatically added'''
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	'''a new user needs to be activate before it can login'''
	is_active = models.BooleanField(_('active'), default=True)
	'''to verify if a new user to be a staff'''
	is_staff = models.BooleanField(_('is_staff'), default=False)
	'''to verify if a new user to be an employee'''
	is_employee = models.BooleanField(default=False)
	'''to verify if a new user to be an employer'''
	is_employer = models.BooleanField(default=False)

	objects = UserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

