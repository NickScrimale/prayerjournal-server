from django.db import models
from .version import Version
from .user import User

class Verse(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    version_id = models.ForeignKey(Version, on_delete=models.CASCADE)
    verse = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)