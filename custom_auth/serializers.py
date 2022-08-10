from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from custom_auth.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, min_length=8, write_only=True)
    # phone_number = serializers.CharField(required=True, min_length=10, max_length=15, write_only=True)

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError(detail='password does not match', code='password_match')
        return attrs

    def validate_username(self, value):
        if MyUser.objects.filter(username=value).exists():
            raise serializers.ValidationError('login already used')
        return value

    def validate_password(self, password):
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e)
        return password

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"]
        )
        # Token.objects.create(user=user)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'password']
