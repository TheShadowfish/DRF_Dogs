from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer, DogDetailSerializer, DogSerializerCreateUpdate
from users.permissions import IsModer


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    filterset_fields = ('breed',)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('date_born',)
    search_fields = ('name',)


    def get_serializer_class(self):
        if self.action == "retrieve":
            return DogDetailSerializer
        if self.action in ["create", "update"]:
            return DogSerializerCreateUpdate
        return DogSerializer

    def perform_create(self, serializer):
        dog = serializer.save()
        dog.owner = self.request.user
        dog.save()

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer,)
        return super().get_permissions()


class BreedCreateAPIView(CreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def perform_create(self, serializer):
        breed = serializer.save(owner=self.request.user)
        # breed.owner = self.request.user
        # breed.save()


class BreedListAPIView(ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedRetrieveAPIView(RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedUpdateAPIView(UpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDestroyAPIView(DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

