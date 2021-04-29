from django.db import models
from users.models import auth,UserProfile

class clients(models.Model):
    auth=models.OneToOneField(auth, on_delete=models.CASCADE, verbose_name='Учетная запись')
    userprof=models.ForeignKey(UserProfile,on_delete=models.RESTRICT, null=True,  verbose_name='Закрепленный сотрудник')
    client_name = models.CharField(max_length=250, verbose_name="Краткое наименование")
    client_number = models.CharField(max_length=250, verbose_name="Номер клиента", null=True, blank=True)
    client_fullname = models.CharField(max_length=250, verbose_name="Полное наименование", null=True, blank=True)
    client_inn = models.CharField(max_length=250, verbose_name="ИНН", null=True, blank=True)
    client_ogrn = models.CharField(max_length=250, verbose_name="ОГРН", null=True, blank=True)
    client_kpp = models.CharField(max_length=250, verbose_name="КПП", null=True, blank=True)
    client_factaddr = models.CharField(max_length=250, verbose_name="Фактический адрес", null=True, blank=True)
    client_juraddr = models.CharField(max_length=250, verbose_name="Юридический адрес", null=True, blank=True)
    client_telephone = models.CharField(max_length=1024, verbose_name="Телефон", null=True, blank=True)
    client_mail = models.CharField(max_length=1024, verbose_name="Почта", null=True, blank=True)
    client_site = models.CharField(max_length=250, verbose_name="Сайт", null=True, blank=True)
    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиенты'
        ordering = ['client_name']



class contact_man(models.Model):
    client = models.ForeignKey('clients', null=True, on_delete=models.CASCADE, verbose_name='Клиент')
    FIO = models.CharField(max_length=250, verbose_name="ФИО", null=True)
    position = models.CharField(max_length=250, verbose_name="Должность", null=True)
    email = models.CharField(max_length=250, verbose_name="Почта", null=True, blank=True)
    telephone = models.CharField(max_length=250, verbose_name="Телефон", null=True, blank=True)
    def __str__(self):
        return str(self.client.client_name) + ' ' + str(self.FIO)

    class Meta:
        verbose_name_plural = 'Контактные лица'
        verbose_name = 'Контактное лицо'


class clientobj(models.Model):
    client = models.ForeignKey('clients', null=True, on_delete=models.CASCADE, verbose_name='Клиент')
    object_name = models.CharField(max_length=250, verbose_name="Объект", null=True)
    object_adress = models.CharField(null=True, max_length=250, verbose_name='Адрес')
    object_telephone = models.CharField(max_length=250, verbose_name="Телефон", null=True)
    object_email = models.CharField(max_length=250, verbose_name="Почта", null=True)
    object_site = models.CharField(max_length=250, verbose_name="Сайт", null=True)

    def __str__(self):
        return self.object_name

    class Meta:
        verbose_name_plural = 'Объекты'
        verbose_name = 'Объект'


class object_contracts(models.Model):
    clientobj = models.ForeignKey(clientobj,null=True, on_delete=models.CASCADE,verbose_name='Объект',related_name='clientobj')
    object_contracts = models.FileField(upload_to='contracts/', verbose_name="Договор", null=True,blank=True)
    contracts_name =  models.CharField(max_length=250, verbose_name="Наименование", null=True,blank=True)
    contracts_description = models.CharField(max_length=1024, verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return str(self.clientobj)

    class Meta:
        verbose_name_plural = 'Договора'
        verbose_name = 'Договор'

# Create your models here.
