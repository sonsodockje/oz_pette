# Generated by Django 5.0.3 on 2024-04-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_dog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='max_weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='최대 무게'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='min_weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='최소 무게'),
        ),
    ]