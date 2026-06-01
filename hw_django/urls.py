"""
URL configuration for hw_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from manager_app.views.tasks import create_task, get_tasks, get_id_task, get_tasks_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/create/', create_task),
    path('tasks/', get_tasks),
    path('tasks/<int:pk>/', get_id_task),
    path('tasks/status/', get_tasks_status)
]
