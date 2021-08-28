from rest_framework.viewsets import ViewSet

class DayViewSet(ViewSet):
    def list(self, request):
        # Returns all national days on a given day of the month
        pass
    def retrieve(self, request, pk):
        # Returns specific national day
        pass