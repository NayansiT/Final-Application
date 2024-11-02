from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'email', 'status', 'date_applied') 
    search_fields = ('name', 'email')  
    list_filter = ('status', 'date_applied')  
    ordering = ('date_applied',)  
     

