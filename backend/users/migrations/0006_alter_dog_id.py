# Generated by Django 5.0.3 on 2024-04-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_dogs_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]