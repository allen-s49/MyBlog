from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_tag = models.CharField(max_length=20)
	blog_content = models.TextField()
	pub_date = models.DateTimeField('date published')
	update_date = models.DateTimeField('date updated')
	read_counts = models.IntegerField()