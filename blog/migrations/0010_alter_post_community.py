# Generated by Django 4.2.16 on 2024-09-10 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_vote_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="community",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="blog.community",
            ),
        ),
    ]
