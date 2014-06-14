from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
class User(models.Model):
    summoner = models.CharField(max_length=16)#summoner Name
class Logger(User):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=30)
class Matches(models.Model):
    user = models.ForeignKey(User)
'''
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    #username = models.CharField(max_length=30,blank=True)
    #password = models.CharField(max_length=30,blank=True)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
