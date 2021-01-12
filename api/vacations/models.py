from django.db import models
from users.models import UserProfile
# Create your models here.

class Vacations(models.Model):
    userprof = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Сотрудник')
    start = models.DateField(db_index=True, verbose_name='Дата начала отпуска', null=True, blank=True)
    end = models.DateField(db_index=True, verbose_name='Дата окончания отпуска')


    def __str__(self):
        return self.userprof

    class Meta:
        verbose_name_plural = 'Отпуска'
        verbose_name = 'Отпуск'