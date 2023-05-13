from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fullstackcapapi.models import Prayer, User

class PrayView(ViewSet):
    def retrieve(self, request, pk):
        try:
            prayer = Prayer.objects.get(pk=pk)
            serializer = PrayerSerializer(prayer)
            return Response(serializer.data)
        except Prayer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):

        prayers = Prayer.objects.all()
        serializer = PrayerSerializer(prayers, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        user = User.objects.get(id=request.data["uid"])
        prayer = Prayer.objects.create(
            uid = user,
            content = request.data["content"],
            pub_date = request.data["pub_date"]
        )
            
        serializer = PrayerSerializer(prayer)
        return Response(serializer.data)
            
        
    def update(self, request, pk):
        
        prayer = Prayer.objects.get(pk=pk)
        prayer.uid = User.objects.get(id=request.data["uid"])
        prayer.content = request.data["content"]
        prayer.publ_date = request.data["pub_date"]
        prayer.save()

        serializer = PrayerSerializer(prayer)
        return Response(serializer.data)
    
    def delete(self, request, pk): 
        prayer = Prayer.objects.get(pk=pk)
        prayer.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PrayerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Prayer
            fields = '__all__'
            depth = 1