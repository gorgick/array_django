from django.contrib.postgres.fields import ArrayField
from django.db import models


class Work(models.Model):
    name = models.CharField(max_length=200)
    workdays = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        return self.name
