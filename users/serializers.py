from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'tg_nick', 'avatar', 'groups', 'user_permissions', 'is_superuser', 'is_staff',)

        """
            "id": 1,
    "password": "pbkdf2_sha256$600000$FAVGVNT2SttB55I38wFVD9$erJIMRLv0dO/e73RrLyuzVNaZZTVQSMVWULv+PYUsNY=",
    "last_login": null,
    "is_superuser": false,
    "first_name": "",
    "last_name": "",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2024-07-15T12:10:57.626285Z",
    "email": "test@sky.pro",
    "phone": null,
    "tg_nick": null,
    "avatar": null,
    "groups": [],
    "user_permissions"
        """