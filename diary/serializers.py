from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, DiaryEntry

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation')

    def validate(self, data):
        # Only check password confirmation if it's provided
        if 'password_confirmation' in data and data.get('password') != data.get('password_confirmation'):
            raise serializers.ValidationError({"password": "Passwords don't match"})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)  # Remove if exists
        password = validated_data.pop('password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'username', 'bio', 'created_at', 'updated_at')

class DiaryEntrySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = DiaryEntry
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'username')
        read_only_fields = ('user',) 