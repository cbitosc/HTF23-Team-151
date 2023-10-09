from django.contrib import admin

# Register your models here.
from events.models import Profile,clubevents,emailid

admin.site.register(Profile)
admin.site.register(clubevents)
admin.site.register(emailid)

