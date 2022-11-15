from django.contrib import admin

# Register your models here.
from .models import Round
from .models import Tournament

admin.site.register(Round)
admin.site.register(Tournament)