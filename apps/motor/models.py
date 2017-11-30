from django.contrib import admin
from django.db import models


############################################################################### ModelMotor
class ModelMotor(models.Model):
    idModelMotor = models.AutoField(primary_key=True)
    nameModelMotor = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameModelMotor

    class Meta:
        managed = True
        db_table = "ModelMotor"


@admin.register(ModelMotor)
class ModelMotorAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameModelMotor', 'status',)
    list_display = ('idModelMotor', 'nameModelMotor')
    list_display_links = ('idModelMotor', 'nameModelMotor')
    search_fields = ('idModelMotor', 'nameModelMotor',)
    ordering = ('idModelMotor',)




############################################################################### SeriesMotor
class SeriesMotor(models.Model):
    idSeriesMotor = models.AutoField(primary_key=True)
    nameSeriesMotor = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameSeriesMotor

    class Meta:
        managed = True
        db_table = "SeriesMotor"


@admin.register(SeriesMotor)
class SeriesMotorAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameSeriesMotor', 'status',)
    list_display = ('idSeriesMotor', 'nameSeriesMotor')
    list_display_links = ('idSeriesMotor', 'nameSeriesMotor')
    search_fields = ('idSeriesMotor', 'nameSeriesMotor',)
    ordering = ('idSeriesMotor',)




############################################################################### Motor
class Motor(models.Model):
    idMotor = models.AutoField(primary_key=True)
    nameMotor = models.CharField(max_length=250)
    idModelMotor = models.ForeignKey(ModelMotor, db_column='idModelMotor')
    idSeriesMotor = models.ForeignKey(SeriesMotor, db_column='idSeriesMotor')
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameMotor

    class Meta:
        managed = True
        db_table = "Motor"


@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameMotor', 'status', 'idModelMotor', 'idSeriesMotor', )
    list_display = ('idMotor', 'nameMotor')
    list_display_links = ('idMotor', 'nameMotor')
    search_fields = ('idMotor', 'nameMotor',)
    ordering = ('idMotor',)