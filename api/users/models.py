from django.contrib.auth.models import AbstractUser
from django.db import models


class auth(AbstractUser):
    role = ((1, 'Сотрудник'),
            (2, 'Клиент'))
    status = models.IntegerField(verbose_name='Роль', choices=role, default=1, null=True,blank=True)


# Create your models here.
class UserProfile(models.Model):
    auth = models.OneToOneField(auth, on_delete=models.CASCADE, verbose_name='Учетная запись')
    first_name = models.CharField(max_length=150, blank=True, null=True,verbose_name='Имя')
    last_name = models.CharField(max_length=150, blank=True, null=True,verbose_name='Фамилия')
    thirdname = models.CharField(verbose_name='Отчество', max_length=256, null=True, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=256, null=True, blank=True)
    telephone = models.CharField(verbose_name='Телефон', max_length=256, null=True, blank=True)
    telephone = models.EmailField(verbose_name='Почта', max_length=256, null=True, blank=True)
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    passport = models.CharField(verbose_name='Паспортные данные', null=True, max_length=1024, blank=True)


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


