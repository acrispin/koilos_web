from django.contrib import admin
from django.db import models


############################################################################### Worker
class Worker(models.Model):
    idWorker = models.AutoField(primary_key=True)
    nameWorker = models.CharField(max_length=250)
    firstLastNameWorker = models.CharField(max_length=250)
    secondLastNameWorker = models.CharField(max_length=250)
    dniWorker = models.CharField(max_length=250)
    status = models.CharField(max_length=3, default="A")
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameWorker

    class Meta:
        managed = True
        db_table = "Worker"


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameWorker', 'firstLastNameWorker', 'secondLastNameWorker', 'dniWorker', 'status',)
    list_display = ('idWorker', 'nameWorker')
    list_display_links = ('idWorker', 'nameWorker')
    search_fields = ('idWorker', 'nameWorker',)
    ordering = ('idWorker',)




############################################################################### Assistant
class Assistant(models.Model):
    idAssistant = models.AutoField(primary_key=True)
    nameAssistant = models.CharField(max_length=250)
    firstLastNameAssistant = models.CharField(max_length=250)
    secondLastNameAssistant = models.CharField(max_length=250)
    dniAssistant = models.CharField(max_length=20)
    status = models.CharField(max_length=3, default="A")
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameAssistant

    class Meta:
        managed = True
        db_table = "Assistant"


@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameAssistant', 'firstLastNameAssistant', 'secondLastNameAssistant', 'dniAssistant', 'status',)
    list_display = ('idAssistant', 'nameAssistant')
    list_display_links = ('idAssistant', 'nameAssistant')
    search_fields = ('idAssistant', 'nameAssistant',)
    ordering = ('idAssistant',)

