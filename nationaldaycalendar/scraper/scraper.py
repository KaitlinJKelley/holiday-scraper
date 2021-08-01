from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from datetime import date
import calendar
import re

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

            html_decoded = html_bytes.decode("utf-8")

            soup = BeautifulSoup(html_decoded, 'html.parser')

            # Search by ID to get div tags containing national day information
            div = soup.find(id="et-boc")

            div_text = div.get_text()

            # Remove line breaks
            text_list = div_text.split('\n')

            # Remove blank spaces left after split
            days_list = [i for i in text_list if i != '' and i != ' ']

            # Removes spaces converted to regex during scrape
            days_list = [re.sub(r'\xa0', '', string) for string in days_list]

            national_days.append(days_list)

        # Remove list that does not represent a month of national days
        national_days.pop(0)

        print(national_days)

    else:
        # If function is invoked on a date other than the one allowed
        raise Exception("DateError")

get_national_days()