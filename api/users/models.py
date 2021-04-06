from django.contrib.auth.models import AbstractUser
from django.db import models


class auth(AbstractUser):
    role = ((1, 'Сотрудник'),
            (2, 'Клиент'))
    status = models.IntegerField(verbose_name='Роль', choices=role, default=1, null=True)

    class Meta:
        verbose_name = 'Учетная запись'
        verbose_name_plural = 'Учетные записи'
        ordering = ('-is_active',)


class Units(models.Model):
    name = models.CharField(max_length=150, null=True, verbose_name='Наименование отдела')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

class Auto(models.Model):
    userprof = models.ForeignKey('UserProfile', null=False, on_delete=models.CASCADE, verbose_name='Сотрудник')
    name = models.CharField(max_length=150, null=True, verbose_name='Наименование авто')
    autonum = models.CharField(max_length=150, null=True, verbose_name='Номер авто')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомомбили'

    def __str__(self):
        return self.userprof.last_name+' '+self.name+' '+self.autonum

# Create your models here.
class UserProfile(models.Model):
    unit = models.ForeignKey('Units', null=True, on_delete=models.RESTRICT, verbose_name='Отдел')
    auth = models.OneToOneField(auth, on_delete=models.CASCADE, verbose_name='Учетная запись')
    first_name = models.CharField(max_length=150, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=150, null=False, verbose_name='Фамилия')
    thirdname = models.CharField(verbose_name='Отчество', max_length=256, null=False)
    position = models.CharField(verbose_name='Должность', max_length=256, null=True)
    telephone = models.CharField(verbose_name='Телефон', max_length=256, null=True, blank=True)
    #email = models.CharField(verbose_name='Почта', max_length=256, null=True, blank=True)
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    passport = models.CharField(verbose_name='Паспортные данные', null=True, max_length=1024, blank=True)
    other = models.CharField(verbose_name='Примечание', null=True, max_length=1024, blank=True)
    foto = models.ImageField(verbose_name='Изображения', upload_to='user_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('-last_name',)

    def __str__(self):
        if self.first_name is not None:
            if self.last_name is not None:
                if self.thirdname is not None:
                    return self.last_name + ' ' + self.first_name + ' ' + self.thirdname
                else:
                    return self.last_name + ' ' + self.first_name
            else:
                return self.first_name
        else:
            return self.auth
