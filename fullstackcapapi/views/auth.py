from fullstackcapapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):

    uid = request.data['uid']

    try:
        user = User.objects.get(uid=uid)
        data= {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'profile_image_url': user.profile_image_url
        }
        return Response(data)
    except:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)
    
@api_view(['POST'])
def register_user(request):

    user = User.objects.create(
        uid=request.data['uid'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        profile_image_url=request.data['profile_image_url']
    )

    data = {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'profile_image_url': user.profile_image_url
    }
    return Response(data)