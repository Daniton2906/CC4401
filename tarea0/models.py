from django.db import models
from datetime import datetime

# Create your models here.


class Todo(models.Model):
    priority = models.PositiveIntegerField(default=0)
    task = models.TextField(default='')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.task
