from django.db import models
from utils.models import Register
from django.core.cache import cache
from django.core.validators import MaxValueValidator


class SingletonModel(models.Model):
    """
    Abstract class for singleton models.
    """
    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()

        return cache.get(cls.__name__)

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        abstract = True


class Configuration(Register, SingletonModel):
    """
    Configuration
    """
    site_name = models.CharField(verbose_name='Name', max_length=18, default='CellFixStore')
    site_name_mini = models.CharField(verbose_name='Short name', max_length=4, default='CFSP')
    use_site_name = models.BooleanField(verbose_name="Logo names", default=True)
    site_logo = models.ImageField(verbose_name='Logo', upload_to="logos", blank=True, null=True)
    site_logo_mini = models.ImageField(verbose_name='Logo mini', upload_to="logos", blank=True, null=True)
    order_code_sequence = models.IntegerField(verbose_name='Code sequence Work orders',
                                              default=1, validators=[MaxValueValidator(999999999)])

    class Meta:
        verbose_name = "Configuration"

    def __str__(self):
        return "Configuration"
