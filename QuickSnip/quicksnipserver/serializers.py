from .models import urls, clicks
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email', 'first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class urlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = urls
        fields = '__all__'

class clicksSerializer(serializers.ModelSerializer):
    class Meta:
        model = clicks
        fields = '__all__'

    def create(self, validated_data):
        return clicks.objects.create(**validated_data)
