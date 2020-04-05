from django.db import models
from utils.models import Register


class Client(Register):
    """
    Model that represent Clients
    """
    identification = models.CharField(verbose_name="Identification", max_length=13, unique=True)
    name_surname = models.CharField(verbose_name="Names and Surnames", max_length=200, unique=True)
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(verbose_name="Phone", max_length=100)
    address = models.CharField(verbose_name="Address", max_length=250)

    def __str__(self):
        return self.name_surname

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['name_surname']

