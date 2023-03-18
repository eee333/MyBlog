from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name')
        read_only_fields = ['created_at', 'updated_at']