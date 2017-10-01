from __future__ import unicode_literals

from django.db import models

# Create your models here.
class backupFolder(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=200,null=False, unique=True)
    path = models.CharField(max_length=200,null=False, unique=True)
    backupPath = models.CharField(max_length=200,null=False, unique=True)
