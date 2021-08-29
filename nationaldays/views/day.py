import psycopg2
from nationaldays.config.config import config
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class DayViewSet(ViewSet):

    def retrieve(self, request, pk):
        # Returns specific national day
        try:            
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)

            # create a cursor; using RealDictCursor allows data to be accessed by column name
            dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            dict_cur.execute("""
            SELECT id, name, TO_CHAR(date, 'MM-DD-YYYY') as date, day_history, day_about
            FROM nationaldays_day
            WHERE id = (%s)
            """, (pk,))

            national_day = dict_cur.fetchone()

            return Response(national_day)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)