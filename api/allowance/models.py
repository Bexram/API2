from django.db import models
from users.models import UserProfile

# Create your models here.
class allowance(models.Model):
    userprof = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Сотрудник')
    a_name = models.CharField(max_length=250, verbose_name="Наименование допуска")
    a_serial=models.CharField(max_length=250, verbose_name="Серийный номер", null=True)
    a_start = models.DateField(db_index=True, verbose_name='Дата начала допуска')
    a_end = models.DateField(db_index=True, verbose_name='Дата окончания допуска')
    a_status = models.BooleanField(verbose_name='На руках', default=0)
    a_remind=models.BooleanField(verbose_name='Автонапоминание',default=0)
    def __str__(self):
        return self.a_name


    class Meta:
        verbose_name_plural = 'Допуски'
        verbose_name = 'Допуск'
        ordering = ['-a_end']

class itemverification(models.Model):
    v_name = models.CharField(max_length=250, verbose_name="Наименование оборудования")
    v_serial = models.CharField(max_length=250, verbose_name="Серийный номер")
    v_end = models.DateField(db_index=True, verbose_name='Поверка заканчивается')
    v_remind = models.BooleanField(verbose_name='Автонапоминание', default=0)

    def __str__(self):
        return self.v_name


    class Meta:
        verbose_name_plural = 'Поверки'
        verbose_name = 'Поверка'
        ordering = ['-v_end']

class insurance(models.Model):
    userprof = models.ForeignKey(UserProfile,null=True, on_delete=models.CASCADE, verbose_name='Сотрудник')
    i_name = models.CharField(max_length=250, verbose_name="Объект страхования")
    i_start = models.DateField(db_index=True, verbose_name='Дата начала страхования')
    i_end = models.DateField(db_index=True, verbose_name='Дата окончания страхования')
    i_status = models.BooleanField(verbose_name='На руках', default=0)
    i_remind = models.BooleanField(verbose_name='Автонапоминание', default=0)

    def __str__(self):
        return self.i_name


    class Meta:
        verbose_name_plural = 'Страховки'
        verbose_name = 'Страховка'
        ordering = ['-i_end']