from django.db import models

# Create your models here.

class Model(models.Model):
    name = models.CharField(max_length=100)
    content = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
