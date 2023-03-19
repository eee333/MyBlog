from rest_framework import serializers
import re

from users.models import User


class PasswordValidator:
    def __call__(self, value):
        if not (len(value) >= 8 and
                re.search(r'\d+', value) and
                re.search(r'[a-zA-Z]+', value) and not
                re.search(r'\s+', value)):
            raise serializers.ValidationError('Пароль должен быть не менее 8 символов, должен включать цифры!')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[PasswordValidator()])

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, validators=[PasswordValidator()])
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            user = super().update(instance, validated_data)
            user.set_password(user.password)
            user.save()
            return user

        return super().update(instance, validated_data)
