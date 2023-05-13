from django.db import models
from .verses import Verse
from .user import User

class UserLike(models.Model):
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)