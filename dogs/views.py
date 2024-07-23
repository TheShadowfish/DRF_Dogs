from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from dogs.models import Dog, Breed
from dogs.paginations import CustomPagination
from dogs.serializers import DogSerializer, BreedSerializer, DogDetailSerializer, DogSerializerCreateUpdate
from users.permissions import IsModer, IsOwner


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    filterset_fields = ('breed',)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('date_born',)
    search_fields = ('name',)
    pagination_class = CustomPagination

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
        # почему-то удалять отказывался собаку у простого пользователя (не модератора)
        # а создавал без проблем
        if self.request.user.groups.filter(name="moders").exists():

            if self.action in ["create", "destroy"]:
                self.permission_classes = (~IsModer,)
            elif self.action in ["update", "retrieve"]:
                self.permission_classes = (IsModer,)
        elif self.action != "create":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class BreedCreateAPIView(CreateAPIView):
    permission_classes = (IsModer | IsAuthenticated,)
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def perform_create(self, serializer):
        breed = serializer.save(owner=self.request.user)
        # breed.owner = self.request.user
        # breed.save()


class BreedListAPIView(ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    pagination_class = CustomPagination


class BreedRetrieveAPIView(RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (IsModer | IsOwner, IsAuthenticated)


class BreedUpdateAPIView(UpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (IsModer | IsOwner, IsAuthenticated)


class BreedDestroyAPIView(DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (IsOwner | ~IsModer, IsAuthenticated)
