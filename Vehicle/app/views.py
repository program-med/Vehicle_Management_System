from django.http import HttpResponse

from .models import Vehicle


def home(request):
    return HttpResponse('Vehicle management application is running.')


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    lines = [f"{vehicle.brand} — {vehicle.formatted_price} — {vehicle.vehicle_info()}" for vehicle in vehicles]
    content = '<br>'.join(lines) if lines else 'No vehicles available.'
    return HttpResponse(content)
