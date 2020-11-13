from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(blocks)
admin.site.register(floors)
admin.site.register(room)
# admin.site.register(student)
admin.site.register(warden)
admin.site.register(student_room)