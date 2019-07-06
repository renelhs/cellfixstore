from django.db import models
from utils.models import Register
from decimal import Decimal


class Product(Register):
    """
    Model that represent Products and Services
    """
    TYPE = (
        ('product', 'PRODUCT'),
        ('service', 'SERVICE')
    )
    
    code = models.CharField(verbose_name='Code', unique=True, max_length=20)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    value = models.DecimalField(verbose_name='Value', max_digits=6, decimal_places=2,
                                default=Decimal('0.00'))
    type = models.CharField(verbose_name='Type', max_length=7, choices=TYPE, default='SERVICE')

    def __str__(self):
        return self.name + ' | ' + str(self.value)

    class Meta:
        ordering = ['code']

