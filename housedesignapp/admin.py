from django.contrib import admin
from housedesignapp.models import Project, Appointment, Inbox

# Register your models here.

admin.site.register(Project)
admin.site.register(Appointment)
admin.site.register(Inbox)