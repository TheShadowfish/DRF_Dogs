from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from dogs.models import Dog, Breed


class BreedSerializer(ModelSerializer):
    dogs = SerializerMethodField()

    def get_dogs(self, obj):
        return [dog.name for dog in Dog.objects.filter(breed=obj)]

    class Meta:
        model = Breed
        fields = "__all__"


class DogSerializer(ModelSerializer):
    breed = BreedSerializer(read_only=True)
    class Meta:
        model = Dog
        fields = "__all__"


class DogDetailSerializer(ModelSerializer):
    count_dog_with_same_breed = SerializerMethodField()
    breed = BreedSerializer(read_only=True)

    def get_count_dog_with_same_breed(self, obj):
        return Dog.objects.filter(breed=obj.breed).count()

    class Meta:
        model = Dog
        fields = ('name', 'breed', 'description', 'photo', 'date_born', 'count_dog_with_same_breed')


