from django.contrib import admin

# Register your models here.
from events.models import Profile,clubevents

admin.site.register(Profile)
admin.site.register(clubevents)

