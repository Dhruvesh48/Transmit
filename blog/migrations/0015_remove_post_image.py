# Generated by Django 4.2.16 on 2024-09-15 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_post_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image",
        ),
    ]
