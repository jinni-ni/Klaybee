# Generated by Django 3.2.8 on 2021-10-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('externalapi', '0003_auto_20211010_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token_address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
