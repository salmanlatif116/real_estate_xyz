# Generated by Django 5.1 on 2024-09-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Rating'),
        ),
    ]
