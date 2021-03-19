from django.db import models
from clients.models import object_contracts, clientobj, contact_man
from users.models import UserProfile

# Create your models here.
class QReport(models.Model):
    clientobj = models.ForeignKey(clientobj, on_delete=models.CASCADE, verbose_name='Объект')
    contact_man=models.ForeignKey(contact_man, on_delete=models.CASCADE, verbose_name='Контактное лицо')
    userprof=models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Сотрудник')
    name = models.CharField(max_length=1024, verbose_name="Наименование", null=True)
    works= models.CharField(max_length=1024, verbose_name="Работы", null=True)
    project = models.CharField(max_length=250, verbose_name="Проект", null=True, default='Неустановлено')
    dateproj = models.CharField(max_length=250, verbose_name="Дата проекта", null=True, default='Неустановлено')
    results = models.CharField(max_length=1024, verbose_name="Результат проверки", null=True)
    rep_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    auto_generate=models.BooleanField(verbose_name='Автоформирование', default=1)

    def __str__(self):
        return str(self.clientobj.object_name)

    class Meta:
        verbose_name_plural = 'Отчеты'
        verbose_name = 'Отчет'
        ordering = ['-rep_published']

class ReadyReport(models.Model):
    number=models.IntegerField(verbose_name='Номер',null=True, blank=True)
    clientobj = models.ForeignKey(clientobj, null=True, on_delete=models.CASCADE, verbose_name='Объект')
    contact_man=models.ForeignKey(contact_man, null=True, on_delete=models.CASCADE, verbose_name='Контактное лицо')
    userprof=models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE, verbose_name='Сотрудник')
    works= models.CharField(max_length=1024, verbose_name="Работы", null=True)
    project = models.CharField(max_length=250, verbose_name="Проект", null=True, default='Неустановлено')
    dateproj = models.CharField(max_length=250, verbose_name="Дата проекта", null=True, default='Неустановлено')
    results = models.CharField(max_length=1024, verbose_name="Результат проверки", null=True)
    rep_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    def __str__(self):
        return str(self.clientobj.object_name)

    class Meta:
        verbose_name_plural = 'Сформированные отчеты'
        verbose_name = 'Сформированный отчет'
        ordering = ['-rep_published']