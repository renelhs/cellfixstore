from django.db import models
from utils.models import Register
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from datetime import date
from decimal import Decimal
from client.models import Client
from product.models import Product


class Order(Register):
    """
    Model that represent Orders
    """
    STATES = (
        ('received', 'RECEIVED'),
        ('process', 'PROCESS'),
        ('finished', 'FINISHED'),
        ('delivered', 'DELIVERED'),
        ('cancelled', 'CANCELLED')
    )

    code = models.IntegerField(verbose_name='Code', unique=True, validators=[MaxValueValidator(999999999)],
                               blank=True, null=True)
    date_in = models.DateField(verbose_name="Start date", default=date.today)
    date_out = models.DateField(verbose_name="End date", blank=True, null=True)
    imei = models.CharField(verbose_name="IMEI", max_length=200, blank=True, null=True)
    state = models.CharField(verbose_name="State", max_length=10, default="received", choices=STATES)
    client = models.ForeignKey(Client, verbose_name="Client", on_delete=models.CASCADE, blank=True, null=True)
    service = models.ManyToManyField(Product, verbose_name="Service")
    lock_code = models.CharField(verbose_name="Unlock code", max_length=100, blank=True, null=True)
    total_value = models.DecimalField(verbose_name="Total value", max_digits=6, decimal_places=2,
                                      default=Decimal('0.00'))
    payment = models.DecimalField(verbose_name="Payment", max_digits=6, decimal_places=2, default=Decimal('0.00'))
    balance = models.DecimalField(verbose_name="Balance", max_digits=6, decimal_places=2, default=Decimal('0.00'))
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Receives", on_delete=models.CASCADE,
                                    blank=True, null=True, related_name="%(app_label)s_%(class)s_received_by")
    delivered_to = models.CharField(verbose_name="Delivered to", max_length=10, blank=True, null=True)
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Technician", on_delete=models.CASCADE,
                                   blank=True, null=True, related_name="%(app_label)s_%(class)s_technician")
    service_detail = models.TextField(verbose_name="Service detail", blank=True, null=True)
    observations = models.TextField(verbose_name="Observations", blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.code)

    class Meta:
        ordering = ['-code']
