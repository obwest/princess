# Generated by Django 5.1.1 on 2024-10-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
