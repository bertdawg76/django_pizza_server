from __future__ import unicode_literals
import datetime
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Topping(models.Model):
    topping_name = models.CharField(max_length=100)
    topping_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.topping_name


class Crust(models.Model):
    crust_type = models.CharField(max_length=100)
    crust_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.crust_type


class Size(models.Model):
    size_type = models.CharField(max_length=100)
    size_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.size_type


class Sides(models.Model):
    side_name = models.CharField(max_length=100)
    side_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.side_name

class Order(models.Model):
    user = models.ForeignKey(User, default=1)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    order_time = models.DateTimeField(auto_now_add=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE, null=True)
    sides = models.ManyToManyField(Sides, through='SideNumber', blank=True)


    # sides = models.ManyToManyField(SideOrder, blank=True, through=SideCount)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.size.size_type, self.crust.crust_type)


class SideNumber(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    sides = models.ForeignKey('Sides', on_delete=models.CASCADE)
    side_count = models.IntegerField()


