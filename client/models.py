from django.db import models
from core.models import Person


class Client(Person):
    is_verfied = models.BooleanField(default=False, blank=True)
    total_orders = models.IntegerField(default=0, blank=True)
    has_copon = models.BooleanField(default=False, blank=True)
    sale = models.FloatField(default=0, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="client-photo")

    @property
    def points(self):
        return self.total_orders


class Phone(models.Model):
    person = models.ForeignKey(Client, related_name='phones', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)