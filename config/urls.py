

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dogs/", include("dogs.urls", namespace='dogs')),

]
