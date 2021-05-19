from django.core.management import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from io import BytesIO
from io import TextIOWrapper
import csv
from django.conf import settings
import redis
from datetime import datetime
import json


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)
class Command(BaseCommand):

    help = "Get NhavCopy from BSEIndia Website everyday at 6PM IST"

    def handle(self, *args, **options):
        try:
            print("Hello world")
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            page = requests.get("https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx",headers = headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            dowloadable_link = soup.find(id="ContentPlaceHolder1_btnhylZip")['href']
            zipfile_raw = requests.get(dowloadable_link, headers = headers)
            zip_file = ZipFile(BytesIO(zipfile_raw.content))

            with zip_file.open(zip_file.namelist()[0], 'r') as infile:
                reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
                for data_row in reader:
                    redis_key = data_row[1].strip()
                    value_string = f'{{"date":"{datetime.date(datetime.now())}","code":"{data_row[0]}","open":"{data_row[4]}","high":"{data_row[5]}","low":"{data_row[6]}","close":"{data_row[7]}"}}'
                    redis_instance.lpush(redis_key,value_string)
            print("BhavCopy Loaded Successfully")
        except Exception as e:
            # TODO: Chnage error type
            raise CommandError(e)
