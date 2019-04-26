from django.db import models
from client.models import Client
from driver.models import Driver


class Order(models.Model):
    client = models.ForeignKey(Client, related_name="orders", on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, related_name="orders", null=True, blank=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField(default=0, blank=True)
    time = models.DateTimeField(null=True)
    rate = models.FloatField(default=0, blank=True)
    message = models.TextField()
    location = models.TextField()
    destination = models.TextField()


class OrderPhoto(models.Model):
    order = models.ForeignKey(Order, related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to="order-photo")
