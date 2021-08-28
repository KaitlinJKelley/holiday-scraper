from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import psycopg2
from nationaldays.config.config import config
import datetime

class YearViewSet(ViewSet):
    def list(self, request):
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)

            # create a cursor; using RealDictCursor allows data to be accessed by column name
            dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            dict_cur.execute("""
            SELECT id, date, name, day_history, day_about
            FROM nationaldays_day 
            Order By date
            """)

            national_days = dict_cur.fetchall()

            # {
            #     date: [
            #         {
            #             name: name,
            #             about: about,
            #             history: history
            #         }
            #     ]
            # }

            national_days_dict = {}

            for day in national_days:
                day_dict = {
                    'name': day['name'],
                    'history': day['day_history'],
                    'about': day['day_about']
                }

                str_date = datetime.date.strftime(day['date'], '%m-%d-%Y')

                if str_date not in national_days_dict:
                    # Adds date to dictionary if it isn't already in the dictionary
                    national_days_dict[str_date] = []
                
                # Appends nation day dictionary to list of the date the national day occurs on 
                national_days_dict[str_date].append(day_dict)

            return(Response(national_days_dict))
                
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)