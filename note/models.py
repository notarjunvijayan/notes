from email.policy import default
from re import L
from django.utils import timezone
from django.db import models
# Create your models here.

class note(models.Model):
    Title = models.CharField('Title',max_length = 15)
    Description = models.TextField('Description',max_length = 200)
    Date = models.DateField('Date', default=timezone.now)

    def __str__(self):
        return str(self.Title)