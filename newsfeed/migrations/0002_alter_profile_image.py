# Generated by Django 4.1.2 on 2022-10-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsfeed", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="profile_pics/default0.png", upload_to="profile_pics/"
            ),
        ),
    ]
