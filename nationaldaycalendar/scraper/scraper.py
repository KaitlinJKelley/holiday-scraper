from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from datetime import date
import calendar

def get_national_days():

    today = date.today()

    if today.month == 8 and today.day == 1:

        national_days = []

        months = calendar.month_name
        for month in months:

            url = f"https://nationaldaycalendar.com/{month}/"

            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

            req = urllib.request.Request(url=url, headers=headers)

            page = urlopen(req)

            html_bytes = page.read()
            html = html_bytes.decode("utf-8")

            soup = BeautifulSoup(html, 'html.parser')

            soup = soup.find(id="et-boc")

            soup_text = soup.get_text()

            soup_list = soup_text.split('\n')

            soup_list = [i for i in soup_list if i != '' and i != ' ']

            national_days.append(soup_list)
        
        national_days.pop(0)

        print(national_days)

    else:
        raise Exception("DateError")

get_national_days()