from rest_framework.routers import SimpleRouter
from dogs.apps import DogsConfig
from dogs.views import DogViewSet

router = SimpleRouter()
router.register("", DogViewSet)


app_name = DogsConfig.name


urlpatterns = []

urlpatterns += router.urls