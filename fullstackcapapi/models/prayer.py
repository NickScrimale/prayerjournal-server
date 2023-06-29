from django.db import models
from .user import User
from datetime import datetime

class Prayer(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=800)
    pub_date = models.TextField(max_length=800)