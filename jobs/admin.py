from django.contrib import admin
from .models import Cost

@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['id', 'costModel', 'dateModel']
