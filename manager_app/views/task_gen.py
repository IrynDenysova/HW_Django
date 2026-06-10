# Реализуйте фильтрацию, поиск и сортировку:
# Реализуйте фильтрацию по полям status и deadline.
# Реализуйте поиск по полям title и description.
# Добавьте сортировку по полю created_at.

from django_filters.rest_framework import filters, DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from manager_app.models import Task
from manager_app.serializers import TaskSerializer


class TaskListCreateGenericAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,
                       OrderingFilter]
    filterset_fields = ['status','deadline']
    search_fields = ['title','description']
    ordering_fields = ['created_at']


class TaskListUpdateDeleteGenericAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

