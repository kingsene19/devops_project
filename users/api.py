from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import UserSerializer

@api_view(['GET'])
def rest_api(request):
    if request.method == "GET":
        queryset = User.objects.all()
        ser = UserSerializer(queryset, many=True)
        return Response(ser.data)