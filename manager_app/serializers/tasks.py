# Задание 1: Эндпоинт для создания задачи
# Создайте эндпоинт для создания новой задачи. Задача должна быть создана с полями title, description, status, и deadline.
#
# Шаги для выполнения:
#
# Определите сериализатор для модели Task.
# Создайте представление для создания задачи.
# Создайте маршрут для обращения к представлению.

from rest_framework import serializers
from manager_app.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description', 'status', 'deadline']