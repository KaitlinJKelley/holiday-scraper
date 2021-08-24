from collections import namedtuple
from django.db.models.base import Model
from rest_framework.viewsets import ViewSet
from nationaldays.models.Day import Day
from rest_framework import serializers, status
from rest_framework.response import Response
import psycopg2
from nationaldays.config.config import config

class YearViewSet(ViewSet):
    def list(self, request):
    # try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        # create a cursor
        # cursor = conn.cursor()

        dict_cur.execute("""
        SELECT id, date, name
        FROM nationaldays_day 
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
            day_object = Day()
            day_object.date = day.date
            if day.date in national_days_list:
                national_days_list[day.date].append({
                    'name': day.name,
                    'history': day.day_history,
                    'about': day.day_about
                })
            else:
                national_days_list[day.date] = []

        print(national_days_list)

        return()
            
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        


# class NationalDaySerializer(serializers.ModelSerializer):

#     class Meta:

#         model = Day

#         fields = '__all__'