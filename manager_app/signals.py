from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task


@receiver(pre_save, sender=Task)
def notify_task_status_change(sender, instance, **kwargs):


    if not instance.pk:
        return

    try:
        old_task = Task.objects.get(pk=instance.pk)
    except Task.DoesNotExist:
        return

    if old_task.status == instance.status:
        return

    subject = f"Статус вашей задачи изменён: {instance.title}"
    message = (
        f"Здравствуйте, {instance.owner.username}!\n\n"
        f"Статус вашей задачи был изменён.\n"
        f"Старый статус: {old_task.status}\n"
        f"Новый статус: {instance.status}\n\n"
        f"С уважением,\nСистема управления задачами"
    )

    send_mail(
        subject,
        message,
        None,
        [instance.owner.email],
        fail_silently=False,
    )
