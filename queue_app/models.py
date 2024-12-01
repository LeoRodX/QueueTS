from django.db import models
from datetime import datetime


# Create your models here.
class QueueTab(models.Model):
    data_reg = models.DateField('Дата регистрации', default=datetime.now)
    time_reg = models.TimeField('Время регистрации', default=datetime.now)
    ticket = models.CharField('Номер талона', max_length=200)
    invited = models.DateTimeField('Клиент приглашён', null=True)
    serviced = models.DateTimeField('Обслуживание завершено', null=True)
