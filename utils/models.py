from django.db import models
from django.conf import settings
from crum import get_current_user


class Register(models.Model):
    """
    Abstract class that register changes in all models.
    """
    create_date = models.DateTimeField(verbose_name="Create Date", auto_now_add=True, editable=False)
    write_date = models.DateTimeField(verbose_name="Write Date", auto_now=True, editable=False)
    create_uid = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Create by", editable=False,
                                   on_delete=models.CASCADE, blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_create_uid")
    write_uid = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Write by", editable=False,
                                  on_delete=models.CASCADE, blank=True, null=True,
                                  related_name="%(app_label)s_%(class)s_write_uid")

    def save(self, *args, **kwargs):
        user = get_current_user()

        if not user.is_anonymous:
            if not self.pk:
                self.create_uid = user
                self.write_uid = user
            else:
                self.write_uid = user

        super(Register, self).save(*args, **kwargs)

    class Meta:
        abstract = True
