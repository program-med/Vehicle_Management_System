from django.db import models


class Vehicle(models.Model):
    

    brand = models.CharField(max_length=100)
    price = models.FloatField()

    class Meta:
        ordering = ['brand']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    @property
    def formatted_price(self):
        return f"₱{self.price:,.2f}"

    def vehicle_info(self):
        return f"{self.brand} costs {self.formatted_price}."

    def __str__(self):
        return f"{self.brand} (Vehicle)"


class Car(Vehicle):
    doors = models.IntegerField()

    # Method Overriding
    def vehicle_info(self):
        return f"{self.brand} Car with {self.doors} doors costs {int(self.price)}"


class Motorcycle(Vehicle):
    helmet_included = models.BooleanField(default=True)

    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {int(self.price)}"