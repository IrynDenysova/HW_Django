from django.contrib import admin
from manager_app.models import Task, SubTask, Category

admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Category)
