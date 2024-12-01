# Generated by Django 5.0.6 on 2024-05-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_app', '0002_queuetab_data_reg_queuetab_ticket_b_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuetab',
            name='invited',
            field=models.DateTimeField(verbose_name='Дата и время вызова клиента'),
        ),
        migrations.AlterField(
            model_name='queuetab',
            name='serviced',
            field=models.DateTimeField(verbose_name='Дата и время завершения Облуживания клиента'),
        ),
        migrations.AlterField(
            model_name='queuetab',
            name='ticket_b',
            field=models.CharField(default='Талон', max_length=200),
        ),
    ]