from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=255)

class urls(models.Model):
    url = models.CharField(max_length=255)
    # user = models.ForeignKey(users, on_delete=models.CASCADE)
    short_url = models.CharField(max_length=255, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class clicks(models.Model):
    url = models.ForeignKey(urls, on_delete=models.CASCADE)
    click_timestamp = models.DateTimeField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=0)
    ip_address = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)
