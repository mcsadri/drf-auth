from django.contrib.auth import get_user_model
from django.db import models


class Starship(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    registry = models.CharField(max_length=64)
    ship_class = models.CharField(max_length=64)
    commissioned = models.CharField(max_length=4)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
