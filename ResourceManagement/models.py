from django.db import models


class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ip_address = models.CharField(max_length=32)
    type = models.CharField(max_length=20)
    state = models.BooleanField(default=False)
