# Generated by Django 4.2.2 on 2024-07-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_donation_tg_chat_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="donation",
            name="tg_chat_id",
        ),
        migrations.RemoveField(
            model_name="user",
            name="tg_nick",
        ),
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите телеграм chat-id",
                max_length=50,
                null=True,
                verbose_name="Телеграм chat-id",
            ),
        ),
    ]
