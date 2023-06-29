from rest_framework import generics
from .serializers import StarshipSerializer
from .models import Starship


class StarshipList(generics.ListAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class StarshipDetail(generics.RetrieveAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
