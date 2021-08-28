from collections import namedtuple
from django.db.models.base import Model
from rest_framework.viewsets import ViewSet
from nationaldays.models.Day import Day
from rest_framework import serializers, status
from rest_framework.response import Response
import psycopg2
from nationaldays.config.config import config
from http.client import HTTPResponse
import json
import datetime

class YearViewSet(ViewSet):
    def list(self, request):
    # try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        # create a cursor
        # cursor = conn.cursor()

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

        national_days_list = {}

        for day in national_days:
            day_dict = {
                'name': day['name'],
                'history': day['day_history'],
                'about': day['day_about']
            }

            str_date = datetime.date.strftime(day['date'], '%m-%d-%Y')

            if str_date not in national_days_list:
                national_days_list[str_date] = []
                
            national_days_list[str_date].append(day_dict)

        return(Response(national_days_list))
            
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)