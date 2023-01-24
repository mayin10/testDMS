from django.db import models


class BaseModel(models.Model):
    create_by = models.CharField(max_length=100, default='admin')
    update_by = models.CharField(max_length=100, default='admin')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='creation time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update time')
    is_delete = models.BooleanField(default=False, verbose_name='delete')

    class Meta:
        abstract = True