# Generated by Django 3.0.5 on 2020-06-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(max_length=16, primary_key=True, serialize=False, verbose_name='用户id')),
                ('user_name', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.IntegerField(max_length=32, verbose_name='用户密码')),
            ],
        ),
    ]
