from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Starship


class StarshipTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_starship = Starship.objects.create(
            owner=testuser1,
            name='Kobayashi Maru',
            registry='none',
            ship_class='Class III neutronic fuel carrier',
            commissioned='n/a',
        )
        test_starship.save()

    # class 32
    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_starships_model(self):
        starship = Starship.objects.get(id=1)
        actual_owner = str(starship.owner)
        actual_name = str(starship.name)
        actual_registry = str(starship.registry)
        actual_ship_class = str(starship.ship_class)
        actual_commissioned = str(starship.commissioned)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Kobayashi Maru")
        self.assertEqual(actual_registry, "none")
        self.assertEqual(actual_ship_class, "Class III neutronic fuel carrier")
        self.assertEqual(actual_commissioned, "n/a")

    def test_get_starship_list(self):
        url = reverse("starship_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        starships = response.data
        self.assertEqual(len(starships), 1)
        self.assertEqual(starships[0]["name"], "Kobayashi Maru")

    def test_get_starship_by_id(self):
        url = reverse("starship_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        starship = response.data
        self.assertEqual(starship["name"], "Kobayashi Maru")

    def test_create_starship(self):
        url = reverse("starship_list")
        data = {
            "owner": 1,
            "name": "HMS Bounty",
            "registry": "none",
            "ship_class": "B'rel-class",
            "commissioned": "2286"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        starships = Starship.objects.all()
        self.assertEqual(len(starships), 2)
        self.assertEqual(Starship.objects.get(id=2).name, "HMS Bounty")

    def test_update_starship(self):
        url = reverse("starship_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Phoenix",
            "registry": "none",
            "ship_class": "Prototype warp ship",
            "commissioned": "2063"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        starship = Starship.objects.get(id=1)
        self.assertEqual(starship.name, data["name"])
        self.assertEqual(starship.owner.id, data["owner"])
        self.assertEqual(starship.registry, data["registry"])
        self.assertEqual(starship.ship_class, data["ship_class"])
        self.assertEqual(starship.commissioned, data["commissioned"])

    def test_delete_starship(self):
        url = reverse("starship_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        starships = Starship.objects.all()
        self.assertEqual(len(starships), 0)

    # class 32
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("starship_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
