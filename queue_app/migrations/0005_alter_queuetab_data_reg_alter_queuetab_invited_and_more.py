# Generated by Django 5.0.6 on 2024-05-09 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_app', '0004_remove_queuetab_ticket_b_alter_queuetab_data_reg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuetab',
            name='data_reg',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='queuetab',
            name='invited',
            field=models.DateTimeField(verbose_name='Клиент приглащён'),
        ),
        migrations.AlterField(
            model_name='queuetab',
            name='serviced',
            field=models.DateTimeField(verbose_name='Обслуживание завершено'),
        ),
        migrations.AlterField(
            model_name='queuetab',
            name='ticket',
            field=models.CharField(max_length=200, verbose_name='Номер талона'),
        ),
        migrations.AlterField(
            model_name='queuetab',
            name='time_reg',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Время регистрации'),
        ),
    ]
