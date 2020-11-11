from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import dacobj,dacmatrix
from .serializers import MenuSerializer
# Create your views here.

class MenuList(APIView):
    """
    Перечисляет все сниппеты или создает новый сниппет.
    """
    premissions=[IsAuthenticated]
    def get(self, request, format=None):
        queryset = dacmatrix.objects.filter(subjects=request.user)
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)

