# from rest_framework.reverse import reverse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dogs.models import Breed, Dog
from users.models import User


class DogTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.breed = Breed.objects.create(name='Лабрадор', breed="Большая мохнатая красивая белая собака")
        self.dog = Dog.objects.create(name="Гром", breed=self.breed, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_dog_retrieve(self):
        url = reverse("dogs:dog-detail", args=(self.dog.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), self.dog.name)

    def test_dog_create(self):
        url = reverse("dogs:dog-list")
        data = {"name": "Форест"}
        response = self.client.post(url, data)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.all().count(), 2)

