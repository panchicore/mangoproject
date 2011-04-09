
from contacts.models import ContactHistory
from contacts.models import Contact
from django.contrib import admin

#class PersonAdmin(admin.ModelAdmin):
#    list_display = ('user','location','old_id', 'created', 'modified')
#    search_fields = ('user__username',)
#    raw_id_fields = ('user',)

admin.site.register(Contact)
admin.site.register(ContactHistory)