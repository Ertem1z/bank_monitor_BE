# Generated by Django 3.0.5 on 2020-06-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0004_auto_20200623_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
