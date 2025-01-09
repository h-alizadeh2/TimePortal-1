from django.contrib import admin
from .models import(
    Time_Destination,
    Time_Type,
)
# Register your models here.
class Admin_Time_Destination(admin.ModelAdmin):
    list_display = [
        'name',
        'type'
    ]

admin.site.register(Time_Destination,Admin_Time_Destination)

class Admin_Time_Type(admin.ModelAdmin):
        list_display = [
            'type'
        ]
admin.site.register(Time_Type, Admin_Time_Type)