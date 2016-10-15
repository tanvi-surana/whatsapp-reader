from __future__ import unicode_literals
import os
from django.db import models

# Create your models here.
class Document(models.Model):
	docfile = models.FileField(upload_to='uploaded_files/')
	def __str__(self):
		return os.path.basename(self.docfile.name)
	class Meta:
		verbose_name = 'docfile'
		verbose_name_plural = 'docfiles'
  
 


# Tag include is not about inserting something from model into your template. Is about inserting content of specified template. You need to write custom template filter which will read your file content and return it into template:

# from django import template

# register = template.Library()

# @register.filter
# def print_file_content(f):
#     try:
#         return f.read()
#     except IOError:
#         return ''
# And use it into template like:

# <div>{{ object.file1|print_file_content }}</div>
# Or you can pass it through template context. Then just read file content into your view and add this content to your template context dictionary.



#http://django-filer.readthedocs.org/en/latest/usage.html