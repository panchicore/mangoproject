from django_extensions.db.fields import ModificationDateTimeField
from django_extensions.db.fields import CreationDateTimeField
from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=False, blank=True)
    phone = models.CharField(max_length=10)
    mobil = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return self.name

class ContactHistory(models.Model):
    contact = models.ForeignKey(Contact, related_name='history')
    history = models.CharField(max_length=255, choices=( ('llame','Llame'),('no-llame','No Llame'),('escribi','Escribi Email') ) )
    created = CreationDateTimeField()
    edited = ModificationDateTimeField()

    def __unicode__(self):
        return 'Yo %s a %s (%s)' % (self.history, self.contact, self.created)