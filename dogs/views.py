from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from dogs.models import Breed, Dog
from dogs.paginations import CustomPagination
from dogs.serializers import (BreedSerializer, DogDetailSerializer,
                              DogSerializer, DogSerializerCreateUpdate)
from dogs.tasks import send_information_about_like
from users.permissions import IsModer, IsOwner


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="description from swagger_auto_schema via method_decorator"
    ),
)
class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    filterset_fields = ("breed",)
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ("date_born",)
    search_fields = ("name",)
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        dog = serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DogDetailSerializer
        if self.action in ["create", "update"]:
            return DogSerializerCreateUpdate
        return DogSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

        # почему-то удалять отказывался собаку у простого пользователя (не модератора)
        # а создавал без проблем
        # if self.request.user.groups.filter(name="moders").exists():
        #
        #     if self.action in ["create", "destroy"]:
        #         self.permission_classes = (~IsModer,)
        #     elif self.action in ["update", "retrieve"]:
        #         self.permission_classes = (IsModer,)
        # elif self.action != "create":
        #     self.permission_classes = (IsOwner,)
        # return super().get_permissions()

    @action(detail=True, methods=("post",))
    def likes(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        if dog.likes.filter(pk=request.user.pk).exists():
            dog.likes.remove(request.user)
            # send_information_about_like.delay()
        else:
            dog.likes.add(request.user)
            send_information_about_like.delay(dog.owner.email)
        serializer = self.get_serializer(dog)
        return Response(data=serializer.data)


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
