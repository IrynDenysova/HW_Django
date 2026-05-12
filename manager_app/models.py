# Реализовать модели:
# Модель Task:
# Описание: Задача для выполнения.
# Поля:
# title: Название задачи. Уникально для даты.
# description: Описание задачи.
# categories: Категории задачи. Многие ко многим.
# status: Статус задачи. Выбор из: New, In progress, Pending, Blocked, Done
# deadline: Дата и время дедлайн.
# created_at: Дата и время создания. Автоматическое заполнение.
# Модель SubTask:
# Описание: Отдельная часть основной задачи (Task).
# Поля:
# title: Название подзадачи.
# description: Описание подзадачи.
# task: Основная задача. Один ко многим.
# status: Статус задачи. Выбор из: New, In progress, Pending, Blocked, Done
# deadline: Дата и время дедлайн.
# created_at: Дата и время создания. Автоматическое заполнение.
# Модель Category:
# Описание: Категория выполнения.
# Поля:
# name: Название категории.

from django.db import models

class Task(models.Model):
    status_choices = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(choices=status_choices, max_length=100, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class SubTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    status = models.CharField(choices=Task.status_choices, max_length=100, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

