from django.contrib import admin
from .models import Clock_In, Clock_Out

admin.site.register(Clock_In)
admin.site.register(Clock_Out)
