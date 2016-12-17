from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_content = models.TextField()
	pub_date = models.DateTimeField('date published')
	update_date = models.DateTimeField('date updated')