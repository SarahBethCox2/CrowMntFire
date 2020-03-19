from django.contrib import admin
from .models import Citizen
from .models import Volunteer
# Register your models here.
 
admin.site.register(Citizen)
admin.site.register(Volunteer)