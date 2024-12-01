from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import QueueTab


class QueueTabAdmin(admin.ModelAdmin):
    fields = ['data_reg', 'time_reg', 'ticket', 'invited', 'serviced']


admin.site.register(QueueTab, QueueTabAdmin)
