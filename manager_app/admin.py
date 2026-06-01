from django.contrib import admin
from manager_app.models import Task, SubTask, Category

# admin.site.register(Task)
# admin.site.register(SubTask)
# admin.site.register(Category)


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskInline]

    list_display = ('id','short_title','created_at','status','deadline')
    list_filter = ('categories','created_at','status')
    search_fields = ('title',)

    @admin.display(description="Name")
    def short_title(self, obj):
        if len(obj.title) > 10:
            return obj.title[:10] + "..."
        return obj.title



@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'task', 'status', 'deadline')
    list_filter = ('task', 'created_at', 'status')
    search_fields = ('title',)
    actions = ['make_done']

    @admin.action(description="Mark as Done")
    def make_done(self, request, queryset):
        queryset.update(status="Done")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ("name",)




