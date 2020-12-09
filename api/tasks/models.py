from django.db import models
from clients.models import object_contracts,clientobj
from users.models import auth

# Create your models here.
class Task(models.Model):
    userprof = models.ForeignKey(auth, on_delete=models.CASCADE, verbose_name='Сотрудник')
    contract = models.ForeignKey(object_contracts, null=True, on_delete=models.CASCADE, verbose_name='Договор')
    Task_name = models.CharField(max_length=250, verbose_name="Задача")
    Task_other = models.TextField(null=True, verbose_name='Примечание',blank=True)
    task_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    task_start = models.DateTimeField(db_index=True, verbose_name='Дата начала задачи', null=True, blank=True)
    task_compl = models.DateTimeField(db_index=True, verbose_name='Дата выполнения')
    task_status = models.BooleanField(verbose_name='Статус', null=0)

    def __str__(self):
        return self.Task_name

    def get_stask(self):
        return self.stask_set.all()

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-task_compl']


class Stask(models.Model):
    Task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, verbose_name='Задача')
    Stask_name = models.CharField(max_length=250, verbose_name="Подзадача")
    stask_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    stask_compl = models.DateTimeField(db_index=True, verbose_name='Дата выполнения')
    Stask_other = models.CharField(max_length=1024, verbose_name="Описание", )
    stask_status = models.BooleanField(verbose_name='Статус', null=0)

    def __str__(self):
        return self.Stask_name

    class Meta:
        verbose_name_plural = 'Подзадачи'
        verbose_name = 'Подзадача'
        ordering = ['-stask_compl']


class Stask_foto(models.Model):
    Stask = models.ForeignKey('Stask', on_delete=models.CASCADE, null=True, verbose_name='Задача')
    foto=models.ImageField(verbose_name='Изображения',upload_to='report_images')

    def __str__(self):
        return str(self.Stask.Stask_name)

    class Meta:
        verbose_name_plural = 'Изображения подзадач'
        verbose_name = 'Изображение'

