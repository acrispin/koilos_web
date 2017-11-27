from django.contrib import admin
from django.db import models


###############################################################################
class ModelMachine(models.Model):
    idModelMachine = models.AutoField(primary_key=True)
    nameModelMachine = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameModelMachine

    class Meta:
        managed = True
        db_table = "ModelMachine"


@admin.register(ModelMachine)
class ModelMachineAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameModelMachine', 'status',)
    list_display = ('idModelMachine', 'nameModelMachine')
    list_display_links = ('idModelMachine', 'nameModelMachine')
    search_fields = ('idModelMachine', 'nameModelMachine',)
    ordering = ('idModelMachine',)




###############################################################################
class SeriesMachine(models.Model):
    idSeriesMachine = models.AutoField(primary_key=True)
    nameSeriesMachine = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameSeriesMachine

    class Meta:
        managed = True
        db_table = "SeriesMachine"


@admin.register(SeriesMachine)
class SeriesMachineAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameSeriesMachine', 'status',)
    list_display = ('idSeriesMachine', 'nameSeriesMachine')
    list_display_links = ('idSeriesMachine', 'nameSeriesMachine')
    search_fields = ('idSeriesMachine', 'nameSeriesMachine',)
    ordering = ('idSeriesMachine',)




###############################################################################
class Machine(models.Model):
    idMachine = models.AutoField(primary_key=True)
    nameMachine = models.CharField(max_length=250)
    idModelMachine = models.ForeignKey(ModelMachine, db_column='idModelMachine')
    idSeriesMachine = models.ForeignKey(SeriesMachine, db_column='idSeriesMachine')
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameMachine

    class Meta:
        managed = True
        db_table = "Machine"


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameMachine', 'status', 'idModelMachine', 'idSeriesMachine', )
    list_display = ('idMachine', 'nameMachine')
    list_display_links = ('idMachine', 'nameMachine')
    search_fields = ('idMachine', 'nameMachine',)
    ordering = ('idMachine',)