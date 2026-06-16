from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from manager_app.models import Category
from manager_app.serializers.categories import CategoryListSerializer, CategoryCreateSerializer, \
    CategoryUpdateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        elif self.action == 'create':
            return CategoryCreateSerializer
        elif self.action in {'update','partial_update'}:
            return CategoryUpdateSerializer
        return CategoryListSerializer

    @action(detail=False, methods=['get'])
    def count_tasks(self, request: Request, *args, **kwargs) -> Response:
        categories = self.get_queryset()
        data = categories.values('id', 'name').annotate(count_tasks=Count('tasks'))
        return Response(data=data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


