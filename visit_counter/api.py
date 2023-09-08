from .models import Visit
from .serializers import VisitSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def count_visits(request):
    if request.method == "GET":
        queryset = Visit.objects.all()
        visit = queryset.get(id=1)
        ser = VisitSerializer(visit)
        return Response(ser.data)
