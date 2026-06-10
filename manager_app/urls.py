from django.urls import path
from rest_framework.views import APIView

from manager_app.views.SubTask_gen import SubTaskListCreateSerializerGenericAPIView, \
    SubtaskListUpdateDeleteGenericAPIView
from manager_app.views.subtasks import SubTaskListCreateView
from manager_app.views.task_gen import TaskListCreateGenericAPIView, TaskListUpdateDeleteGenericAPIView
from manager_app.views.tasks import create_task, get_tasks, get_id_task, get_tasks_status



urlpatterns = [
    # path('tasks/', create_task),
    path('tasks/',TaskListCreateGenericAPIView.as_view()),
    path('tasks/<int:pk>/',TaskListUpdateDeleteGenericAPIView.as_view()),
    # path('tasks/', get_tasks),
    # path('tasks/<int:pk>/', get_id_task),
    path('tasks/status/', get_tasks_status),
    path('subtasks/',SubTaskListCreateSerializerGenericAPIView.as_view()),
    path('subtasks/<int:pk>',SubtaskListUpdateDeleteGenericAPIView.as_view())
    # path('subtasks', SubTaskListCreateView.as_view(),name="subtask-list-create")
]