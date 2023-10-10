from django.contrib import admin
from .models import *

admin.site.register(record)
admin.site.register(completedrecord)

admin.site.site_header = 'Лепесток'