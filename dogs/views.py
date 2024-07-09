from rest_framework.viewsets import ModelViewSet

from dogs.models import Dog
from dogs.serializers import DogSerializer


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

