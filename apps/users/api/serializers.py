from rest_framework import serializers
from apps.users.models import Account

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