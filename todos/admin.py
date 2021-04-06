from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_completed', 'user']

admin.site.register(Item, ItemAdmin)