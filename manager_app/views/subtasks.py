# Задание 5: Создание классов представлений
# Создайте классы представлений для работы с подзадачами (SubTasks), включая создание, получение, обновление и удаление подзадач. Используйте классы представлений (APIView) для реализации этого функционала.
#
# Шаги для выполнения:
#
# Создайте классы представлений для создания и получения списка подзадач (SubTaskListCreateView).
# Создайте классы представлений для получения, обновления и удаления подзадач (SubTaskDetailUpdateDeleteView).
# Добавьте маршруты в файле urls.py, чтобы использовать эти классы.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manager_app.models import SubTask
from manager_app.serializers import SubTaskCreateSerializer
from manager_app.serializers.TaskDetails import SubTaskSerializer


class SubTaskListCreateView(APIView):

    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        subtasks = SubTask.objects.all()
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)


