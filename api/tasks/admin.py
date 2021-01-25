from django.contrib import admin
from .models import Task,Stask,Stask_foto,Reglament,Reglament_cat,trasfer_task
# Register your models here.
admin.site.register(Task)
admin.site.register(Stask)
admin.site.register(Stask_foto)
admin.site.register(Reglament)
admin.site.register(Reglament_cat)
admin.site.register(trasfer_task)