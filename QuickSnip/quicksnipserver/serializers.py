from .models import users, urls, clicks
from rest_framework import serializers

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['pk', 'username', 'password_hash']

class urlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = urls
        fields = ['url', 'short_url', 'date_created', 'date_updated']

class clicksSerializer(serializers.ModelSerializer):
    class Meta:
        model = clicks
        fields = ['pk', 'url', 'click_timestamp', 'number_of_clicks', 'ip_address', 'user_agent', 'referrer', 'country', 'city', 'timezone']
