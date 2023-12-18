from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=50, required=True)
    password_hash = models.CharField(max_length=255, required=True)

class urls(models.Model):
    url = models.CharField(max_length=255, required=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    short_url = models.CharField(max_length=255, required=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class clicks(models.Model):
    url = models.ForeignKey(urls, on_delete=models.CASCADE)
    click_timestamp = models.DateTimeField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=0, max = 200)
    ip_address = models.CharField(max_length=255, required=True)
    user_agent = models.CharField(max_length=255, required=True)
    referrer = models.CharField(max_length=255, required=True)
    country = models.CharField(max_length=255, required=True)
    city = models.CharField(max_length=255, required=True)
    timezone = models.CharField(max_length=255, required=True)
