from rest_framework import serializers  # converts django models to JSON
from .models import Starship # the model to be serialized (aka translated to JSON)


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Starship
