from django.db import models
from django.contrib.auth.models import User

# Create your models here
class urls(models.Model):
    url = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    short_url = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class clicks(models.Model):
    url = models.ForeignKey(urls, on_delete=models.CASCADE)
    click_timestamp = models.DateTimeField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=1)
