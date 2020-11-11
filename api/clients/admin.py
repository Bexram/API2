from django.contrib import admin
from .models import clients,clientobj,contact_man,object_contracts
# Register your models here.
admin.site.register(clients)
admin.site.register(clientobj)
admin.site.register(contact_man)
admin.site.register(object_contracts)