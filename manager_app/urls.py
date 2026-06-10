from django.urls import path
from manager_app.views.subtasks import SubTaskListCreateView
from manager_app.views.tasks import create_task, get_tasks, get_id_task, get_tasks_status




urlpatterns = [
    path('tasks/create/', create_task),
    path('tasks/', get_tasks),
    path('tasks/<int:pk>/', get_id_task),
    path('tasks/status/', get_tasks_status),
    path('subtasks', SubTaskListCreateView.as_view(),name="subtask-list-create")
]