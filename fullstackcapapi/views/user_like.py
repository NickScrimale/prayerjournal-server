from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fullstackcapapi.models import UserLike, Verse, User

class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLike
        fields = ('id', 'user_id', "verse_id")
        depth = 1

class LikeView(ViewSet):
    def retrieve(self, request, pk):
        try:
            user_like = UserLike.objects.get(pk=pk)
            serializer = UserLikeSerializer(user_like)
            return Response(serializer.data)
        except UserLike.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        user_likes = UserLike.objects.all()
        verse = request.query_params.get('verse', None)
        if verse is not None:
            user_likes = user_likes.filter(verse_id=verse)

        serializer = UserLikeSerializer(user_likes, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        user_like = UserLike.objects.get(pk=pk)
        user_like.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        user = User.objects.get(id=request.data["uid"])
        verse = Verse.objects.get(pk=request.data["verse_id"])

        user_like = UserLike.objects.create(
            verse=verse,
            user=user
        )
        serializer = UserLikeSerializer(user_like)
        return Response(serializer.data)

    def destroy(self, request, pk):
        user_like = UserLike.objects.get(pk=pk)
        user_like.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)