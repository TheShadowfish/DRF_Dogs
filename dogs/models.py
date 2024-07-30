from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название породы",
        help_text="Введите название породы",
    )
    breed = models.TextField(
        verbose_name="Описание породы", help_text="Введите описание породы", **NULLABLE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца"
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name


class Dog(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца собаки"
    )

    name = models.CharField(
        max_length=100, verbose_name="Кличка", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Порода",
        help_text="Введите породу собаки",
        **NULLABLE,
        related_name="dogs"
    )
    description = models.TextField(
        verbose_name="Описание собаки", help_text="Введите описание собаки", **NULLABLE
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
        **NULLABLE
    )
    date_born = models.DateField(
        **NULLABLE, verbose_name="Дата рождения", help_text="Укажите дату рождения"
    )
    likes = models.ManyToManyField(
        User,
        **NULLABLE,
        verbose_name="Лайки",
        help_text="Укажите лайки",
        related_name="user_likes",
    )


    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.name
