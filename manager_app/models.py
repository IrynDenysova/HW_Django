from django.db import models

class Task(models.Model):
    status_choices = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
    ]

    days_of_week = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    title = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(choices=status_choices, max_length=100, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    days_of_week = models.CharField(choices=days_of_week, max_length=100,
                                    default='monday',null=True,
                                    blank=True,verbose_name="Day of Week")

    # Модель Task:
    # Добавить метод str, который возвращает название задачи.
    # Добавить класс Meta с настройками:
    # Имя таблицы в базе данных: 'task_manager_task'.
    # Сортировка по убыванию даты создания.
    # Человекочитаемое имя модели: 'Task'.
    # Уникальность по полю 'title'.

    def __str__(self):
         return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'





class SubTask(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    status = models.CharField(choices=Task.status_choices, max_length=100, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Модель SubTask:
    # Добавить метод str, который возвращает название подзадачи.
    # Добавить класс Meta с настройками:
    # Имя таблицы в базе данных: 'task_manager_subtask'.
    # Сортировка по убыванию даты создания.
    # Человекочитаемое имя модели: 'SubTask'.
    # Уникальность по полю 'title'.

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'Subtask'




class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    # Модель Category:
    # Добавить метод str, который возвращает название категории.
    # Добавить класс Meta с настройками:
    # Имя таблицы в базе данных: 'task_manager_category'.
    # Человекочитаемое имя модели: 'Category'.
    # Уникальность по полю 'name'.

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'








