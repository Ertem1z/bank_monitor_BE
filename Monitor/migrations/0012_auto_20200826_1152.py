# Generated by Django 3.0.5 on 2020-08-26 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0011_auto_20200719_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='network',
            old_name='close_wait_count',
            new_name='dev_io_read_rate',
        ),
    ]