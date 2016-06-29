from django.db import models

# Create your models here.
class ToDos(models.Model):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True)
