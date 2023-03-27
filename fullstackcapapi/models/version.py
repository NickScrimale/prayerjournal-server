from django.db import models

class Version(models.Model):
    label = models.CharField(max_length=50)