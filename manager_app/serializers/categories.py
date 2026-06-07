# Задание 2: Переопределение методов create и update
# Создайте сериализатор для категории CategoryCreateSerializer, переопределив методы create и update для проверки уникальности названия категории. Если категория с таким названием уже существует, возвращайте ошибку валидации.
#
# Шаги для выполнения:
#
# Определите CategoryCreateSerializer в файле serializers.py.
# Переопределите метод create для проверки уникальности названия категории.
# Переопределите метод update для аналогичной проверки при обновлении.
from enum import unique

from rest_framework import serializers
from manager_app.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data["name"]

        if Category.objects.filter(name=name).exists():
             raise serializers.ValidationError(
                {"name": "Категория с таким названием уже существует"})
        return super().create(validated_data)
    

    def update(self, instance, validated_data):
        name = validated_data.get("name", instance.name)

        if Category.objects.exclude(id=instance.id).filter(name=name).exists():
            raise serializers.ValidationError(
                {"name": "Категория с таким названием уже существует"})
        return super().update(instance, validated_data)



