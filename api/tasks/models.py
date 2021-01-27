from django.db import models
from clients.models import object_contracts, clientobj
from users.models import auth


# Create your models here.
class Task(models.Model):
    userprof = models.ForeignKey(auth, on_delete=models.CASCADE, verbose_name='Сотрудник')
    contract = models.ForeignKey(object_contracts, null=True, on_delete=models.CASCADE, verbose_name='Договор')
    Task_name = models.CharField(max_length=250, verbose_name="Задача")
    Task_other = models.TextField(null=True, verbose_name='Примечание', blank=True)
    task_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    task_start = models.DateTimeField(db_index=True, verbose_name='Дата начала задачи', null=True, blank=True)
    task_compl = models.DateTimeField(db_index=True, verbose_name='Дата выполнения')
    task_status = models.BooleanField(verbose_name='Статус', default=0)

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
    Stask_other = models.CharField(max_length=1024, verbose_name="Описание", null=True, blank=True)
    stask_status = models.BooleanField(verbose_name='Статус', null=0)

    def __str__(self):
        return self.Stask_name

    class Meta:
        verbose_name_plural = 'Подзадачи'
        verbose_name = 'Подзадача'
        ordering = ['-stask_compl']


class Stask_foto(models.Model):
    Stask = models.ForeignKey('Stask', on_delete=models.CASCADE, null=True, verbose_name='Задача')
    foto = models.ImageField(verbose_name='Изображения', upload_to='report_images', null=True, blank=True)

    def __str__(self):
        return str(self.Stask)

    class Meta:
        verbose_name_plural = 'Фотоотчет подзадач'
        verbose_name = 'Изображение'


class Reglament_cat(models.Model):
    Cat_name = models.CharField(max_length=250, verbose_name="Подзадача")

    def __str__(self):
        return self.Cat_name

    class Meta:
        verbose_name_plural = 'Категории регламентных работ'
        verbose_name = 'Категория регламентных работ'


class Reglament(models.Model):
    period = ((1, 'Ежедневно'),
              (2, 'Еженедельно'),
              (3, 'Ежемесячно'),
              (4, 'Раз в полгода'),
              (5, 'Ежегодно'),
              (6, 'Другое'),
              )
    cat = models.ForeignKey('Reglament_cat', on_delete=models.CASCADE, verbose_name='Категория')
    Task_name = models.CharField(max_length=250, verbose_name="Вид работы")
    Task_period = models.IntegerField(verbose_name='Переодичность', choices=period, default=3)

    def __str__(self):
        return self.Task_name

    class Meta:
        verbose_name_plural = 'Регламентные работы'
        verbose_name = 'Регламентная работа'
        ordering = ['-cat']

class trasfer_task(models.Model):
    to_user = models.ForeignKey(auth, on_delete=models.RESTRICT, verbose_name='Кому перенос',related_name='to')
    Task = models.ForeignKey(Task, on_delete=models.RESTRICT, verbose_name='Задача')

    def __str__(self):
        return self.Task.Task_name

    class Meta:
        verbose_name_plural = 'Уведомления о переносе'
        verbose_name = 'Уведомление о переносе'
