from django.db import models
from users.models import UserProfile
# Create your models here.

class Vacations(models.Model):
    units = ((1, 'Административный отдел'),
            (2, 'Технический отдел - инженера'),
             (3, 'Технический отдел - Монтажники'),
             (4, 'Отдел продаж'))
    userprof = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Сотрудник')
    start = models.DateField(db_index=True, verbose_name='Дата начала отпуска')
    end = models.DateField(db_index=True, verbose_name='Дата окончания отпуска')
    unit=models.CharField(max_length=250, verbose_name="Отдел",choices=units, default=1, null=True, blank=True)


    def __str__(self):
        return self.userprof

    class Meta:
        verbose_name_plural = 'Отпуска'
        verbose_name = 'Отпуск'
