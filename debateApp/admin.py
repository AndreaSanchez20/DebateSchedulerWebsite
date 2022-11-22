from django.contrib import admin

# Register your models here.
from .models import Round2
from .models import Tournament

admin.site.register(Round2)
admin.site.register(Tournament)