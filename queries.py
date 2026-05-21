import os
import django
from datetime import timedelta, datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_django.settings')
django.setup()

from manager_app.models import Task, SubTask

""" 1. Создание записей:
Task:
title: "Prepare presentation".
description: "Prepare materials and slides for the presentation".
status: "New".
deadline: Today's date + 3 days."""


# Task.objects.create(
#     title="Prepare presentation",
#     description="Prepare materials and slides for the presentation",
#     status= "New",
#     deadline=datetime.today() + timedelta(days=3)
# )

""" 2. Создание записей:
SubTasks для "Prepare presentation":
title: "Gather information".
description: "Find necessary information for the presentation".
status: "New".
deadline: Today's date + 2 days.
title: "Create slides".
description: "Create presentation slides".
status: "New".
deadline: Today's date + 1 day."""



# main_task = Task.objects.get(id=2)
#
# SubTask.objects.create(
#     task=main_task,
#     title="Gather information",
#     description="Find necessary information for the presentation",
#     status="New",
#     deadline=datetime.today() + timedelta(days=2)
# )
#
# SubTask.objects.create(
#     task=main_task,
#     title="Create slides",
#     description="Create presentation slides",
#     status="New",
#     deadline=datetime.today() + timedelta(days=1)
# )

""" 3. Чтение записей:
Tasks со статусом "New":
Вывести все задачи, у которых статус "New". """

# task_new = Task.objects.filter(status='New')
# for task in task_new:
#     print(task)

# SubTasks с просроченным статусом "Done":
# Вывести все подзадачи, у которых статус "Done", но срок выполнения истек.

# subtask_status = SubTask.objects.filter(status='Done',
#                                         deadline__lte=datetime.now())
# for subtask in subtask_status:
#     print(subtask)

""" 4. Изменение записей:
Измените статус "Prepare presentation" на "In progress"."""

# Task.objects.filter(
#     title = "Prepare presentation" ).update(status = "In progress")


""" Измените срок выполнения для "Gather information" на два дня назад."""

# SubTask.objects.filter(title="Gather information").update(deadline=datetime.now())

""" Измените описание для "Create slides" на "Create and format presentation slides"."""

# SubTask.objects.filter(title="Create slides").update(description="Create and format presentation slides")

""" 5. Удаление записей:
Удалите задачу "Prepare presentation" и все ее подзадачи."""

# Task.objects.filter(title="Prepare presentation").delete()

