from django.db import models
from users.models import auth
class dacobj(models.Model):
    dacobjects = models.CharField(verbose_name='Модули', max_length=256)
    modulehref = models.CharField(verbose_name='Ссылка', max_length=256, null=True)
    sort=models.IntegerField(verbose_name="Порядок сортировки", unique=True, null=True)

    def __str__(self):
        return self.dacobjects

    class Meta:
        verbose_name_plural = 'Модули'
        verbose_name = 'Модуль'
        ordering=['sort']


class dacmatrix(models.Model):
    level = ((1, 'Чтение'),
             (2, 'Редактирование'))
    subjects = models.ForeignKey(auth, null=True, on_delete=models.CASCADE,
                                 verbose_name='Сотрудник')
    dacobjects = models.ForeignKey('dacobj', related_name='dacobj', on_delete=models.PROTECT, null=True,
                                   verbose_name='Модули')
    acceslevel = models.IntegerField(verbose_name='Уровень доступа', choices=level, default=1)

    def __str__(self):
        return str(self.subjects.username) + ' к ' + str(self.dacobjects.dacobjects) + ' ' + str(self.acceslevel)

    class Meta:
        verbose_name_plural = 'Доступы'
        verbose_name = 'Доступ'
