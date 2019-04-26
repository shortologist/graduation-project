from django.db import models
from core.models import Person


class Driver(Person):
    total_orders = models.IntegerField(default=0, blank=True)
    orders_this_month = models.IntegerField(default=0, blank=True)
    salary = models.FloatField(default=0, blank=True)

    @property
    def rate(self):
        rsum = 0
        for rate in self.orders.rate:
            rsum += rate
        return rsum/self.total_orders


class Photo(models.Model):
    person = models.ForeignKey(Driver, related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="driver-photo")


class Phone(models.Model):
    person = models.ForeignKey(Driver, related_name='phones', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)