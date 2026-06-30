from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manager_app.models import SubTask
from manager_app.permissions import IsOwnerOrReadOnly
from manager_app.serializers import SubTaskCreateSerializer
from manager_app.serializers.TaskDetails import SubTaskSerializer
from rest_framework.pagination import PageNumberPagination


class SubTaskListCreateView(APIView, PageNumberPagination):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    list_size = 5

    def get(self, request):
        task_name = request.query_params.get("task_name")
        status_filter = request.query_params.get("status")

        subtasks = SubTask.objects.all().order_by("-created_at")

        if task_name:
            subtasks = subtasks.filter(task__title__icontains=task_name)

        if status_filter:
            subtasks = subtasks.filter(status=status_filter)

        page = self.paginate_queryset(subtasks, request, view=self)
        serializer = SubTaskSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)


class SubTaskDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_object(self, pk):
        try:
            return SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return None

    def get(self, request, pk):
        subtask = self.get_object(pk)
        if subtask is None:
            return Response({"error": "SubTask is not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        subtask = self.get_object(pk)
        if subtask is None:
            return Response({"error": "SubTask is not found"}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, subtask)
        serializer = SubTaskCreateSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        subtask = self.get_object(pk)
        if subtask is None:
            return Response({"error": "SubTask is not found"}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, subtask)
        serializer = SubTaskCreateSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subtask = self.get_object(pk)
        if subtask is None:
            return Response({"error": "SubTask is not found"}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, subtask)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
