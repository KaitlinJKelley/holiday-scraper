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

            div = soup.find(id="et-boc")

            div_text = div.get_text()

            text_list = div_text.split('\n')

            days_list = [i for i in text_list if i != '' and i != ' ']

            national_days.append(days_list)
        
        national_days.pop(0)

        print(national_days)

    else:
        raise Exception("DateError")

get_national_days()