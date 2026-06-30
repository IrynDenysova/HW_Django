# Задание 1: Переопределение полей сериализатора
# Создайте SubTaskCreateSerializer, в котором поле created_at будет доступно только для чтения (read_only).




from rest_framework import serializers
from manager_app.models import SubTask


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ['created_at', 'owner']