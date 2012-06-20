from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from django.utils import timezone

# user = User.objects.create_user('Matt', 'mgraham@problemsolutions.net', 'mypas5word')
# user.is_staff = True
# user.save()

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	def __unicode__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Blog(models.Model):
	post = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	owner = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.post

class Comment(models.Model):
	post = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published')
	owner = models.ForeignKey(UserProfile)
	blog_post = models.ForeignKey(Blog)
	
	def __unicode__(self):
		return self.post
