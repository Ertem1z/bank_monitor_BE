# Generated by Django 3.0.5 on 2020-08-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warning', '0005_auto_20200826_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='percentilethresholds',
            name='available_memory_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='available_memory_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='available_memory_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='cpu_system_used_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='cpu_system_used_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='cpu_system_used_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='cpu_user_used_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='cpu_user_used_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='cpu_user_used_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='swap_usage_rate_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='swap_usage_rate_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='swap_usage_rate_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='tcp_active_opens_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='tcp_active_opens_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='tcp_active_opens_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='tcp_passive_opens_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='tcp_passive_opens_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='percentilethresholds',
            name='tcp_passive_opens_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='available_memory_t1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='available_memory_t2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='available_memory_t3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='cpu_system_used_t1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='cpu_system_used_t2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='cpu_system_used_t3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='cpu_user_used_t1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='cpu_user_used_t2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='cpu_user_used_t3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='swap_usage_rate_t1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='swap_usage_rate_t2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='swap_usage_rate_t3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='tcp_active_opens_t1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='tcp_active_opens_t2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='tcp_active_opens_t3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='tcp_passive_opens_t1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='tcp_passive_opens_t2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thresholds',
            name='tcp_passive_opens_t3',
            field=models.FloatField(default=0),
        ),
    ]
