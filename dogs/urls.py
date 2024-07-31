from django.urls import path
from rest_framework.routers import SimpleRouter
from dogs.apps import DogsConfig
from dogs.views import (
    DogViewSet,
    BreedCreateAPIView,
    BreedListAPIView,
    BreedUpdateAPIView,
    BreedRetrieveAPIView,
    BreedDestroyAPIView,
)

router = SimpleRouter()
router.register("", DogViewSet)


app_name = DogsConfig.name


urlpatterns = [
    path("breeds/", BreedListAPIView.as_view(), name="breeds-list"),
    path("breeds/<int:pk>/", BreedRetrieveAPIView.as_view(), name="breeds-retrieve"),
    path("breeds/<int:pk>/update/", BreedUpdateAPIView.as_view(), name="breeds-update"),
    path("breeds/create/", BreedCreateAPIView.as_view(), name="breeds-create"),
    path(
        "breeds/<int:pk>/delete/", BreedDestroyAPIView.as_view(), name="breeds-delete"
    ),
]

urlpatterns += router.urls
