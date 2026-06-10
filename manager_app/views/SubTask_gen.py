# Замените классы представлений для подзадач на Generic Views:
# Используйте ListCreateAPIView для создания и получения списка подзадач.
# Используйте RetrieveUpdateDestroyAPIView для получения, обновления и удаления подзадач.
# Реализуйте фильтрацию, поиск и сортировку:
# Реализуйте фильтрацию по полям status и deadline.
# Реализуйте поиск по полям title и description.
# Добавьте сортировку по полю created_at.

from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from manager_app.models import SubTask
from manager_app.serializers import SubTaskCreateSerializer
from manager_app.serializers.TaskDetails import SubTaskSerializer


class SubTaskListCreateSerializerGenericAPIView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,
                       OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

class SubtaskListUpdateDeleteGenericAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

