from rest_framework.serializers import ModelSerializer

from users.models import User, Donation


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # если ограничить поля то пользователь создается некорректно и зайти под ним нельзя. ХЗ что с этим делать. Пароль ДОЛЖЕН БЫТЬ в выводе.
        #  ('id', 'email', 'phone', 'tg_nick', 'avatar', 'groups', 'user_permissions', 'is_superuser', 'is_staff',)

class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"
