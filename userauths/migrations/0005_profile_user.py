# Generated by Django 4.2.2 on 2024-02-05 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userauths", "0004_remove_profile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
