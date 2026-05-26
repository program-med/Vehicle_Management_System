from django.contrib import admin

from .models import Car, Motorcycle, Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'formatted_price', 'vehicle_type')
    search_fields = ('brand',)
    ordering = ('brand',)

    def vehicle_type(self, obj):
        return obj.__class__.__name__

    vehicle_type.short_description = 'Type'


@admin.register(Car)
class CarAdmin(VehicleAdmin):
    list_display = ('brand', 'doors', 'formatted_price')
    search_fields = ('brand',)


@admin.register(Motorcycle)
class MotorcycleAdmin(VehicleAdmin):
    list_display = ('brand', 'helmet_included', 'formatted_price')
    list_filter = ('helmet_included',)
