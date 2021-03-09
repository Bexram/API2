from django.contrib import admin
from . import models
admin.site.register(models.UserProfile)
admin.site.register(models.auth)
admin.site.register(models.Units)
admin.site.register(models.Auto)

