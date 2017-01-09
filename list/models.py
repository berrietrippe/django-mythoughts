from django.db import models
from django.utils import timezone

# Create your models here.
class Quote(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
