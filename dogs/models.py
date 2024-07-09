from django.db import models

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

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name


class Dog(models.Model):
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
        verbose_name="Описание собаки",
        help_text="Введите описание собаки",
        **NULLABLE
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
    count_views = models.PositiveBigIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    owner = models.ForeignKey(D_user, verbose_name='Владелец', help_text='Укажите владельца собаки', **NULLABLE, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]
        permissions=[
            ("can_edit_breed", "Can edit breed"),
            ("can_edit_description", "Can edit description"),

        ]

    def __str__(self):
        return self.name