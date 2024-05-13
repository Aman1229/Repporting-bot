from django.contrib.auth.models import User
from django.db import models


class ExportList(models.Model):
    export = models.CharField('export', max_length=255)

    def __str__(self):
        return (self.export)