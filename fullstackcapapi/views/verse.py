from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fullstackcapapi.models import Verse, User, Version

class VerseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Verse
            fields = '__all__'
            depth = 1

class VerseView(ViewSet):
    """Viewset for verse requests"""
    def list(self, request):
        verses = Verse.objects.all()

        verse_version = request.query_params.get('version', None)
        if verse_version is not None:
            verses = verses.filter(version_id=verse_version)

        verse_user = request.query_params.get('user', None)
        if verse_user is not None:
            verses = verses.filter(user_id=verse_user)

        verse_like = request.query_params.get('liked', None)
        if verse_like is not None:
            verses = verses.filter(liked_id=verse_like)

        serializer = VerseSerializer(verses, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        try:
            verse = Verse.objects.get(id=pk)
            serializer = VerseSerializer(verse)
            return Response(serializer.data)
        except Verse.DoesNotExist as e:
            return Response({'message': e.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        """Handle POST requests for a single post"""
        user = User.objects.get(id=request.data["user_id"])
        version = Version.objects.get(id=request.data["version_id"])
        verse = Verse.objects.create(
            verse = request.data["verse"],
            content = request.data["content"],
            uid = user,
            version_id = version
            )
        serializer = VerseSerializer(verse)
        return Response(serializer.data)
    
    def update(self, request, pk):
        "Handle PUT requests for a single post"""
        verse = Verse.objects.get(pk=pk)
        verse.user_id = User.objects.get(id=request.data["user_id"])
        verse.verse = request.data["verse"]
        verse.version_id = Version.objects.get(id=request.data["version_id"])
        verse.content = request.data["content"]
        verse.save()
        
        serializer = VerseSerializer(verse)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        """Handle DELETE requests for a single post"""
        verse = Verse.objects.get(pk=pk)
        verse.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    


    