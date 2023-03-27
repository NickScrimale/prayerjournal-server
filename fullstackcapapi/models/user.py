from django.db  import models

class User(models.Model):
  uid = models.CharField(max_length=50)
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  profile_image_url = models.CharField(max_length=200)