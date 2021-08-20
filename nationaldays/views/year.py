from django.db.models.base import Model
from rest_framework.viewsets import ViewSet
from nationaldays.models.Day import Day
from rest_framework import serializers, status
from rest_framework.response import Response

class YearViewSet(ViewSet):
    def list(self, request):
        national_days = Day.objects.all()

        serializer = NationalDaySerializer(national_days ,many=True, context={'request': request})

        return Response(serializer.data)

class NationalDaySerializer(serializers.ModelSerializer):

    class Meta:

        model = Day

        fields = '__all__'