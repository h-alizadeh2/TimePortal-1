from django.contrib import admin
from .models import(
    Skill,
    Time_Traveler
)
# Register your models here.

class Admin_Time_Traveler(admin.ModelAdmin):
    list_display = [
        'name',
        'last_name',
        'phone',
        'email',
    ]

admin.site.register(Time_Traveler, Admin_Time_Traveler)
    
class Admin_Skill(admin.ModelAdmin):
    list_display = [
        'skill'
    ]
admin.site.register(Skill, Admin_Skill)

