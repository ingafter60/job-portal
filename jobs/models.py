# jobs/models.py

# DJANGO MODULES
from django.db import models
from django.template.defaultfilters import slugify
from job import settings

# CREATE CUSTOME MODELS HERE

# CATEGORY MODEL
class Category(models.Model):

	'''category title'''
	title = models.CharField(max_length=300) 
	'''category slug is a kind of category title https://jobportal.com/web-design
	   but this tabel field will not be seen in admin panel
	'''
	slug = models.SlugField(default=None, editable=False)


	'''displaying human readable objects as title (category title)'''
	def __str__(self):
		return self.title

	'''offeriding save function to save category title as slug'''
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)	

	'''defining job_count function to count numbers of job in each category'''
	def job_count(self):
		'''attache job to category based on its related_name (line:66)'''
		# return self.jobs.all().count() * 1000	
		return self.jobs.all().count()


# JOB MODEL
class Job (models.Model):

	'''job title'''
	title = models.CharField(max_length=300) 
	'''company name that over the job'''
	company = models.CharField(max_length=300) 
	'''job types'''
	CHOICES = (
		('full_time', 'Full Time'),
		('part_time', 'Part Time'),
		('freelance', 'Freelance'),
		('internship', 'Internship'),
		('temporary', 'Temporary'),
	)
	job_type = models.CharField(choices=CHOICES, max_length=20, blank=False, default=None) 
	'''job location'''
	location = models.CharField(max_length=200, blank=False, default=None)
	'''job description'''
	description = models.TextField(blank=False, default=None)
	'''job publishing date'''
	publishing_date = models.DateTimeField(auto_now_add=True)
	'''job slug is a kind of job title https://jobportal.com/web-design
	   but this tabel field will not be seen in admin panel
	'''
	slug = models.SlugField(default=None, editable=False)
	'''many-to-one relationship: employer can publish 0 or Many jobs'''
	employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
	'''add ONE-TO-MANY or MANY-TO-ONE relationship of the Category and Product models'''
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs', default=None)
	
	'''displaying human readable objects as title (job title)'''
	def __str__(self):
		return self.title

	'''offeriding save function to save job title as slug'''
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Job, self).save(*args, **kwargs)	

	'''ordering the display of job titles by LIFO or DESC'''
	class Meta:
		ordering = ('-id',)	

