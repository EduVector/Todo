from rest_framework import serializers
from apps.users.models import Account
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=6, write_only=True)

    class Meta:
        model = Account
        fields = (
            'id',
            'username',
            'full_name',
            'phone_number',
            'email',
            'password',
        )
    
    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            "username",
            "full_name",
            "phone_number",
            "date_birth",
            "email",
            "gender",
            "is_active",
            "date_created",
        ]


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=225, write_only=True)
    password = serializers.CharField(min_length=3, max_length=16, write_only=True)
    tokens = serializers.SerializerMethodField()

    @staticmethod
    def get_tokens(obj):
        return Account.objects.filter(username=obj.get('username')).first().tokens
    
    class Meta: 
        model = Account
        fields = (
            "id",
            "username",
            "password",
            "tokens"
        )
    
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({"success": False, "message": "Username or password did not match!"})
        data = {
            "success": True,
            "tokens": user.tokens
        }
        return attrs
