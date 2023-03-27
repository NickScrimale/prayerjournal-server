from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fullstackcapapi.models import Prayer

class PrayView(ViewSet):
    def retrieve(self, request, pk):
        try:
            prayer = Prayer.objects.get(pk=pk)
            serializer = PraySerializer(prayer)
            return Response(serializer.data)
        except Prayer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)