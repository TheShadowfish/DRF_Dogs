from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from dogs.models import Breed, Dog
from dogs.validators import validate_forbidden_words


class BreedSerializer(serializers.ModelSerializer):
    dogs = SerializerMethodField()

    def get_dogs(self, obj):
        return [dog.name for dog in Dog.objects.filter(breed=obj)]

    class Meta:
        model = Breed
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    name = serializers.CharField(validators=[validate_forbidden_words])

    class Meta:
        model = Dog
        fields = "__all__"


class DogSerializerCreateUpdate(serializers.ModelSerializer):

    name = serializers.CharField(validators=[validate_forbidden_words])

    class Meta:
        model = Dog
        fields = "__all__"


class DogDetailSerializer(serializers.ModelSerializer):
    count_dog_with_same_breed = SerializerMethodField()
    breed = BreedSerializer(read_only=True)
    name = serializers.CharField(validators=[validate_forbidden_words])

    def get_count_dog_with_same_breed(self, obj):
        return Dog.objects.filter(breed=obj.breed).count()

    class Meta:
        model = Dog
        fields = (
            "name",
            "breed",
            "description",
            "photo",
            "date_born",
            "count_dog_with_same_breed",
        )
