from django.db.models import Q, Count
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework import status


from manager_app.models import Task
from manager_app.serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Задание 1:
# Написать, или обновить, если уже есть, эндпоинт на получение списка всех задач по дню недели.
# Если никакой параметр запроса не передавался - по умолчанию выводить все записи.
# Если был передан день недели (например вторник) - выводить список задач только на этот день недели.
# @api_view(['GET'])
# def get_tasks(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)

class DayOfTasksAPIView(APIView):
    def get(self, request):
        day = request.query_params.get('days_of_tasks')
        if day:
            tasks = Task.objects.filter(days_of_tasks=day.lower())
        else:
            tasks = Task.objects.all()
        if not tasks:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)







@api_view(['GET'])
def get_id_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            {"error": "Task is not found"},
            status=status.HTTP_404_NOT_FOUND

        )
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_tasks_status(request):

    now = timezone.now()


    stats = Task.objects.aggregate(
        total_tasks=Count('id'),
        status_new=Count('id', filter=Q(status='new')),
        status_in_progress=Count('id', filter=Q(status='in_progress')),
        status_pending=Count('id', filter=Q(status='pending')),
        status_blocked=Count('id', filter=Q(status='blocked')),
        status_done=Count('id', filter=Q(status='done')),
        overdue_tasks=Count('id', filter=Q(deadline__lt=now) & ~Q(status='done'))
    )

    response_data = {
        "total": stats['total_tasks'],
        "by_status": {
            "new": stats['status_new'],
            "in_progress": stats['status_in_progress'],
            "pending": stats['status_pending'],
            "blocked": stats['status_blocked'],
            "done": stats['status_done']
        },
        "overdue": stats['overdue_tasks']
    }

    return Response(response_data, status=status.HTTP_200_OK)
