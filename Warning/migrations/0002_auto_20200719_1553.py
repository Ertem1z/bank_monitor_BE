# Generated by Django 3.0.5 on 2020-07-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='percentilethresholds',
            name='available_memory_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='available_memory_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='available_memory_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='close_wait_count_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='close_wait_count_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='close_wait_count_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_system_used_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_system_used_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_system_used_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_used_total_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_used_total_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_used_total_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_user_used_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_user_used_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='cpu_user_used_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='mem_usage_rate_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='mem_usage_rate_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='mem_usage_rate_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='swap_usage_rate_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='swap_usage_rate_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='swap_usage_rate_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='tcp_active_opens_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='tcp_active_opens_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='tcp_active_opens_p3',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='tcp_passive_opens_p1',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='tcp_passive_opens_p2',
            field=models.FloatField(default=0.75),
        ),
        migrations.AlterField(
            model_name='percentilethresholds',
            name='tcp_passive_opens_p3',
            field=models.FloatField(default=0.75),
        ),
    ]
