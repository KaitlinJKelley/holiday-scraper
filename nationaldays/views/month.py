from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class MonthViewSet(ViewSet):
    def day_all(self, month):
        # Returns all national days on a given day of the month
        return Response({'Good':'url'})
    def retrieve(self, request, pk):
        # Returns specific national day
        pass