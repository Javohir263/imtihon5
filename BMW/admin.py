from django.contrib import admin
from .models import Car, Owner
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'color')
    search_fields = ('name', 'model')
    list_filter = ('year', 'color')
    ordering = ('name',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'car')
    search_fields = ('name', 'email')
    list_filter = ('car',)
    ordering = ('name',)

