from django.urls import path
from rest_framework.routers import DefaultRouter

from manager_app.views.categories import CategoryViewSet
from manager_app.views.subtasks import SubTaskListCreateView
from manager_app.views.tasks import create_task, get_id_task, get_tasks_status, DayOfTasksAPIView

router = DefaultRouter()
router.register(r'categories' , CategoryViewSet)

urlpatterns = [
    path('tasks/create/', create_task),
    path('tasks/', DayOfTasksAPIView.as_view(), name='days_of_tasks'),
    path('tasks/<int:pk>/', get_id_task),
    path('tasks/status/', get_tasks_status),
    path('subtasks', SubTaskListCreateView.as_view(),name="subtask-list-create"),
    path("subtasks/filter/", SubTaskListCreateView.as_view(), name="subtask-filtered-list"),

]