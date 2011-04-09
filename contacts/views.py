from urllib2 import Request
from django.shortcuts import render_to_response
from mangoproject.contacts.models import Contact
# Create your views here.

def view_all(request):
    contacts = Contact.objects.all()
    return render_to_response('contacts/views_all.html', {'contacts':contacts})
