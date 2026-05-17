from django.contrib import admin
from manager_app.models import Task, SubTask, Category

# admin.site.register(Task)
# admin.site.register(SubTask)
# admin.site.register(Category)

# Настройте отображение моделей в админке:
# В файле admin.py вашего приложения добавьте классы администратора
# для настройки отображения моделей Task, SubTask и Category.
# Зафиксируйте изменения в гит:
# Создайте новый коммит и запушьте его в ваш гит.
# Создайте записи через админку:
# Создайте суперпользователя.
# Перейдите в административную панель Django.
# Добавьте несколько объектов для каждой модели.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('id','title','created_at','status','deadline')
    list_filter = ('categories','created_at','status')
    search_fields = ('title',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','task','status','deadline')
    list_filter = ('task','created_at','status')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("name",)




