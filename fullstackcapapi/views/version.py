from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fullstackcapapi.models import Version

class VersionView(ViewSet):
    def retrieve(self, request, pk):
        try:
            version = Version.objects.get(pk=pk)
            serializer = VerSerializer(version)
            return Response(serializer.data)
        except Version.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        versions = Version.objects.all()
        serializer = VerSerializer(versions, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        version = Version.objects.get(pk=pk)
        version.label = request.data["label"]
        version.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        version = Version.objects.create(
            label=request.data["label"]
        )
        serializer = VerSerializer(version)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        version = Version.objects.get(pk=pk)
        version.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class VerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('id', 'label')
        depth = 1