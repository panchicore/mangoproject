from django.contrib.auth.models import User
from django.db import models

#TODO - hacer los perfiles con django-userna
#https://django-userena.org/
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    facebook_url = models.URLField()

