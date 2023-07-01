from rest_framework import generics
from .serializers import StarshipSerializer
from .models import Starship


class StarshipList(generics.ListCreateAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class StarshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
