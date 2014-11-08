from django.db import models

# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField("auth.User")
	
