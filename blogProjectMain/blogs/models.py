from django.db import models
from django.contrib.auth.models import User

# user = User.objects.create_user('Matt', 'mgraham@problemsolutions.net', 'mypas5word')
# user.is_staff = True
# user.save()

class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	password = models.CharField(max_length=10)

class Blog(models.Model):
	text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	owner = models.ForeignKey(User)

class Comment(models.Model):
	text = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published')
	owner = models.ForeignKey(User)
	blog_post = models.ForeignKey(Blog)
