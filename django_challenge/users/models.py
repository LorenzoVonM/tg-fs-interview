from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)