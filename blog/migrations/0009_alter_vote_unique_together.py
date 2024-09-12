# Generated by Django 4.2.16 on 2024-09-10 16:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0008_vote"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="vote",
            unique_together={("user", "post")},
        ),
    ]
