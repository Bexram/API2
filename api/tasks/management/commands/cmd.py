from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
            url = 'https://calendar.yoip.ru/2021-calendar.html'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            year = soup.find_all('div', class_='col-6 col-sm-6 col-md-4 text-center')
            holydays=[]
            holydaysp = []
            monthnumb=1
            for month in year:
                for tag in month.find_all('td', class_='_hd warning'):
                    holydays.append('2021-'+str(monthnumb)+'-'+tag.text)
                for tag in month.find_all('td', class_='_hd warning tt-hd'):
                    holydaysp.append('2021-'+str(monthnumb)+'-'+tag.text)
                monthnumb=monthnumb+1

            print('Выполнено обновление календаря')
            f = open('holidays.txt', 'w')
            f.write('hd')
            f.write(str(holydays))
            f.write('hdp')
            f.write(str(holydaysp))
            f.close()
