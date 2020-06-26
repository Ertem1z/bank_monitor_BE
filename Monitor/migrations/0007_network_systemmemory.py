# Generated by Django 3.0.5 on 2020-06-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0006_auto_20200624_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=32)),
                ('tcp_activeopens', models.FloatField()),
                ('tcp_passiveopens', models.FloatField()),
                ('close_wait_count', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=32)),
                ('mem_usage_rate', models.FloatField()),
                ('available_memeory', models.FloatField()),
                ('swap_usage_rate', models.FloatField()),
                ('free_swap_spacecon', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
