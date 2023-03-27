from django.db import models
from .user import User

class Prayer(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, default='Mmm')
    content = models.TextField(max_length=800)