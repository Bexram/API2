from .models import allowance
import datetime
from django.core.mail import send_mail

def mailsender():
    query=allowance.objects.filter(a_end__lte=datetime.datetime.now()+datetime.timedelta(days=30)).filter(a_mailremind=True).filter(a_mail_sended=False)
    for el in query:
        send_mail('Продление '+el.a_name, 'Ваш '+el.a_name+' заканчивается '+str(el.a_end)+', необходимо его продлить до срока окончания.', 'cubp@szsb.ru',
                  [el.userprof.auth.email], fail_silently=False)
        el.a_mail_sended=True
        el.save()
    return 1