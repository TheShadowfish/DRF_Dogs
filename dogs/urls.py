from django.urls import path
from rest_framework.routers import SimpleRouter
from dogs.apps import DogsConfig
from dogs.views import DogViewSet, BreedCreateAPIView, BreedListAPIView, BreedUpdateAPIView, BreedRetrieveAPIView, BreedDestroyAPIView

router = SimpleRouter()
router.register("", DogViewSet)


app_name = DogsConfig.name


urlpatterns = [
    path("breeds/", BreedListAPIView.as_view(), name="breeds_list"),
    path("breeds/<int:pk>/", BreedRetrieveAPIView.as_view(), name="breeds_retrieve"),
    path("breeds/<int:pk>/update/", BreedUpdateAPIView.as_view(), name="breeds_update"),
    path("breeds/create/", BreedCreateAPIView.as_view(), name="breeds_create"),
    path("breeds/<int:pk>/delete/", BreedDestroyAPIView.as_view(), name="breeds_delete"),

]

urlpatterns += router.urls
