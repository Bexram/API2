from django.db import models


# Create your models here.
class Task(models.Model):
    Task_name = models.CharField(max_length=250, verbose_name="Задача")
    Task_other = models.TextField(null=True, verbose_name='Примечание',blank=True)
    task_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    task_compl = models.DateField(db_index=True, verbose_name='Дата выполнения')
    task_status = models.BooleanField(verbose_name='Статус', null=0)

    def __str__(self):
        return self.Task_name

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-task_compl']