from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Secret(models.Model):
    user = models.ForeignKey(User, related_name = "secrets")
    secret = models.CharField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
