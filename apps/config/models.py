from django.contrib import admin
from django.db import models
from apps.general.models import Category, Criteria, DrillBit, Section, SubSection, Polymer, State
from apps.machine.models import Machine
from apps.motor.models import Motor
from apps.person.models import Worker, Assistant


############################################################################### CheckList
class CheckList(models.Model):
    idCheckList = models.AutoField(primary_key=True)
    idCategory = models.ForeignKey(Category, db_column='idCategory')
    idCriteria = models.ForeignKey(Criteria, db_column='idCriteria')
    status = models.CharField(max_length=3, default="A")
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return str(self.idCheckList)

    class Meta:
        managed = True
        db_table = "CheckList"
        unique_together = (('idCategory', 'idCriteria'),)


@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('idCategory', 'idCriteria', 'status', )
    list_display = ('idCheckList', 'idCategory', 'idCriteria', 'status', )
    list_display_links = ('idCheckList', )
    search_fields = ('idCheckList', )
    ordering = ('idCheckList',)




############################################################################### Configuration
class Configuration(models.Model):
    idConfiguration = models.AutoField(primary_key=True)
    idWorker = models.ForeignKey(Worker, db_column='idWorker')
    idAssistant = models.ForeignKey(Assistant, db_column='idAssistant')
    idDrillBit = models.ForeignKey(DrillBit, db_column='idDrillBit')
    idSection = models.ForeignKey(Section, db_column='idSection')
    idSubSection = models.ForeignKey(SubSection, db_column='idSubSection')
    idMachine = models.ForeignKey(Machine, db_column='idMachine')
    idMotor = models.ForeignKey(Motor, db_column='idMotor')
    idPolymer = models.ForeignKey(Polymer, db_column='idPolymer')
    date = models.DateField(null=True, blank=True) #TODO: validar field
    beginingTotalTime = models.DateTimeField(null=True, blank=True) #TODO: validar field
    endingTotalTime = models.DateTimeField(null=True, blank=True) #TODO: validar field
    azimuth = models.IntegerField(null=True, blank=True) #TODO: validar field
    attitude = models.IntegerField(null=True, blank=True) #TODO: validar field
    remiShell = models.IntegerField(null=True, blank=True) #TODO: validar field
    amountPolymer = models.DecimalField(max_digits=10, decimal_places=2, null=True) #TODO: validar field
    amountBentonite = models.DecimalField(max_digits=10, decimal_places=2, null=True) #TODO: validar field
    amountBoxes = models.DecimalField(max_digits=10, decimal_places=2, null=True) #TODO: validar field
    volumeWater = models.IntegerField(null=True, blank=True) #TODO: validar field
    volumeOil = models.IntegerField(null=True, blank=True) #TODO: validar field
    initialDepth = models.IntegerField(null=True, blank=True) #TODO: validar field
    finalDepth = models.IntegerField(null=True, blank=True) #TODO: validar field
    initialHobbs = models.DateTimeField(null=True, blank=True) #TODO: validar field
    finalHobbs = models.DateTimeField(null=True, blank=True) #TODO: validar field
    observations = models.TextField(null=True, blank=True) #TODO: validar field
    status = models.CharField(max_length=3, default="A")
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return str(self.idConfiguration)

    class Meta:
        managed = True
        db_table = "Configuration"


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('idWorker', 'idAssistant', 'idDrillBit', 'idSection', 'idSubSection', \
              'idMachine', 'idMotor', 'idPolymer', 'date', 'beginingTotalTime', \
              'endingTotalTime', 'azimuth', 'attitude', 'remiShell', 'amountPolymer', \
              'amountBentonite', 'amountBoxes', 'volumeWater', 'volumeOil', 'initialDepth', \
              'finalDepth', 'initialHobbs', 'finalHobbs', 'observations', 'status',)
    list_display = ('idConfiguration', 'idWorker', 'idAssistant', 'status', )
    list_display_links = ('idConfiguration', )
    search_fields = ('idConfiguration', 'idWorker', 'idAssistant',)
    ordering = ('idConfiguration', )




############################################################################### Interval
class Interval(models.Model):
    idInterval = models.AutoField(primary_key=True)
    idConfiguration = models.ForeignKey(Configuration, db_column='idConfiguration')
    description = models.TextField(null=True, blank=True)  # TODO: validar field
    initialTime = models.DateTimeField(null=True, blank=True)  # TODO: validar field
    endingTime = models.DateTimeField(null=True, blank=True)  # TODO: validar field
    perforationBegin = models.CharField(max_length=100, null=True, blank=True) # TODO: validar field
    perforationEnd = models.CharField(max_length=100, null=True, blank=True) # TODO: validar field
    trueLengthRod = models.IntegerField(null=True, blank=True)  # TODO: validar field
    status = models.CharField(max_length=3, default="A")
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return str(self.idInterval)

    class Meta:
        managed = True
        db_table = "Interval"


@admin.register(Interval)
class IntervalAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('idConfiguration', 'description', 'initialTime', 'endingTime', \
              'perforationBegin', 'perforationEnd', 'trueLengthRod', 'status', )
    list_display = ('idInterval', 'idConfiguration', 'initialTime', 'endingTime', 'status', )
    list_display_links = ('idInterval', )
    search_fields = ('idInterval', )
    ordering = ('idInterval',)




############################################################################### CheckListResponse
class CheckListResponse(models.Model):
    idCheckListResponse = models.AutoField(primary_key=True)
    idConfiguration = models.ForeignKey(Configuration, db_column='idConfiguration')
    idCategory = models.ForeignKey(Category, db_column='idCategory')
    idCriteria = models.ForeignKey(Criteria, db_column='idCriteria')
    idState = models.ForeignKey(State, db_column='idState')
    observations = models.TextField(null=True, blank=True)  # TODO: validar field
    status = models.CharField(max_length=3, default="A")
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return str(self.idCheckListResponse)

    class Meta:
        managed = True
        db_table = "CheckListResponse"
        unique_together = (('idConfiguration', 'idCategory', 'idCriteria', 'idState'),)


@admin.register(CheckListResponse)
class CheckListResponseAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('idConfiguration', 'idCategory', 'idCriteria', 'idState', 'observations', 'status', )
    list_display = ('idCheckListResponse', 'idConfiguration', 'idCategory', 'idCriteria', 'idState', 'status', )
    list_display_links = ('idCheckListResponse', )
    search_fields = ('idCheckListResponse', )
    ordering = ('idCheckListResponse',)