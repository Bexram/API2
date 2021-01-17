from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
            url = 'https://calendar.yoip.ru/work/2021-proizvodstvennyj-calendar'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('td', class_='_hd warning')
            print('!!!')
            f = open('holidays.txt', 'w')
            f.write(str(quotes))
            f.close()
