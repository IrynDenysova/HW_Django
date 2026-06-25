# Создайте TaskCreateSerializer и добавьте валидацию для поля deadline, чтобы дата не могла быть в прошлом. Если дата в прошлом, возвращайте ошибку валидации.

from django.utils import timezone
from rest_framework import serializers
from manager_app.models import Task

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Deadline не может быть в прошлом")
        return value