from django.db import models
from django.contrib.auth.models import User
import uuid


class ClassRoom(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid1()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.uuid + ' --> ' + self.name
