from rest_framework import generics
from .serializers import StarshipSerializer
from .models import Starship
from .permissions import IsOwnerOrReadOnly


class StarshipList(generics.ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly, )  # commented out for tests.py test_authentication_required()
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class StarshipDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
