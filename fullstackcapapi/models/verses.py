from django.db import models
from .version import Version
from .user import User

class Verse(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, default='Yes')
    version_id = models.ForeignKey(Version, on_delete=models.CASCADE)
    pub_date = models.DateField()
    verse = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)
    