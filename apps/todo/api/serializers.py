from rest_framework import serializers
from apps.todo.models import Todo



class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id', 
            'title',
            'status',
            'notes',
            'created_at',
            'user'
        ]
        extra_kwargs = {
            'created_at': {'read_only': True},
            'user': {'read_only': True}
        }


class TodoListSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()

    def get_status_display(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Todo
        fields = [
            'id', 
            'title',
            'status',
            'status_display',
            'notes',
            'is_done',
            'created_at',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True}
        }


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'status',
            'notes',
            'is_done',
            'created_at',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True}
        }

