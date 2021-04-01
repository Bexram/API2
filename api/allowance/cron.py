from allowance import models
import datetime
from django.core.mail import send_mail

def checkallowance():
    query=models.allowance.objects.filter(a_end__gte=datetime.datetime.now()-datetime.timedelta(days=30)).filter(a_mail_sended=False)
    for el in query:
        f = open('log.txt', 'a')
        f.write('Продление '+el.a_name)
        f.close
        send_mail('Продление '+el.a_name, 'Ваш '+el.a_name+' заканчивается '+el.a_end+', необходимо его продлить до срока окончания.', 'cubp@szsb.ru',
                  [el.userprof.auth.email], fail_silently=False)
        el.a_mail_sended=True
        el.save()
