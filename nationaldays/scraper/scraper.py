from nationaldays.config.config import config
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import calendar
import re
import psycopg2
import datetime

def get_national_days_for_month(month):

    url = f"https://nationaldaycalendar.com/{month}/"

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    req = urllib.request.Request(url=url, headers=headers)

    page = urlopen(req)

    html_bytes = page.read()

    html_decoded = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html_decoded, 'html.parser')

    # Search by ID to get div tags containing national day information
    div = soup.find(id="et-boc").get_text()

    # Remove line breaks
    text_list = div.split('\n')

    # Remove blank spaces left after split
    days_list = [i for i in text_list if i != '' and i != ' ' and i!= "  "]

    # Removes spaces converted to regex during scrape
    days_list = [re.sub(r'\xa0', ' ', string) for string in days_list]

    days_list = [i.replace("  ", " ") for i in days_list]

    # October and December don't have titles at index 0, 
    # so only pop(0) if the string does not contain a digit from 1 - 31
    if days_list[0].split(" ")[1].isdigit() == False or int(days_list[0].split(" ")[1]) > 31:
        days_list.pop(0)
    
    # Example of final object
    #     month: {
    #         day of month: [national day, national day]
    #     }

    month_days = {}
    
    for string in days_list:
        try:
            day_check = string.split(" ")

            # August contains a leading space left from replacement of \xa0
            if day_check[0] == "":
                day_check.pop(0)

            day_check = day_check[1]

        except:
            # For single index holidays which will throw an error on the split
            pass

        # Removes suffixes such as st, nd, rd, th from end of numbers (April)
        day_checked = ""
        if len(string.split()) < 3:
            day_checked = [i for i in day_check if i.isdigit()]

        # Join back remaining digits, if any
        if len(day_checked) == 1:
            day_checked.insert(0, "0")
        day_checked = "".join(day_checked)

        try: 
            # Convert string to integer
            int(day_checked)

            # If successful, reassign day
            day = day_checked

            # Add a list to hold national days on this day in this month
            month_days[day] = []
        except:
            # The day didn't change, so add the string onto whatever day we're using
            if "proclamation" not in string.lower():
                month_days[day].append(string)
                  
    return month_days


def update_national_days_for_month():
    pass

# Use this function to set up the initial database
def start_database():
    
    months = list(calendar.month_name)

    # Removes empty string at beginning of list
    months.pop(0)

    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cursor = conn.cursor()
        
	# execute a statement
        # cursor.execute('SELECT version()')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    values = []

    for month in months:
        today = datetime.date.today()
        year=today.year
        month_days = get_national_days_for_month(month)  
        

        for day in month_days:
            try:
                date = (datetime.datetime.strptime(f"{year}-{month}-{day}",'%Y-%B-%d'))

                for nat_day in month_days[day]:
                    values.append((date, nat_day,))
            except ValueError:
                pass
        
    cursor.executemany("INSERT INTO nationaldays_day(date, name) VALUES (%s, %s);", (values))
    conn.commit()
            
 




    