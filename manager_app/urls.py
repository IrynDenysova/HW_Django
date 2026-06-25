from django.urls import path
from rest_framework.routers import DefaultRouter

from manager_app.views.categories import CategoryViewSet
from manager_app.views.subtasks import SubTaskListCreateView, SubTaskDetailView
from manager_app.views.tasks import create_task, get_id_task, get_tasks_status, DayOfTasksAPIView, get_my_tasks, TaskDetailView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('tasks/create/', create_task),
    path('tasks/', DayOfTasksAPIView.as_view(), name='days_of_tasks'),
    path('tasks/my/', get_my_tasks, name='my-tasks'),
    path('tasks/status/', get_tasks_status),
    path('tasks/<int:pk>/', get_id_task),
    path('tasks/<int:pk>/manage/', TaskDetailView.as_view(), name='task-detail'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/filter/', SubTaskListCreateView.as_view(), name='subtask-filtered-list'),
    path('subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),
]

urlpatterns += router.urls