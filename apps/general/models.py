from django.contrib import admin
from django.db import models


############################################################################### State
class State(models.Model):
    idState = models.AutoField(primary_key=True)
    nameState = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameState

    class Meta:
        managed = True
        db_table = "State"


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameState', 'status',)
    list_display = ('idState', 'nameState')
    list_display_links = ('idState', 'nameState')
    search_fields = ('idState', 'nameState',)
    ordering = ('idState',)




############################################################################### Criteria
class Criteria(models.Model):
    idCriteria = models.AutoField(primary_key=True)
    nameCriteria = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameCriteria

    class Meta:
        managed = True
        db_table = "Criteria"


@admin.register(Criteria)
class CriteriaAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameCriteria', 'status',)
    list_display = ('idCriteria', 'nameCriteria')
    list_display_links = ('idCriteria', 'nameCriteria')
    search_fields = ('idCriteria', 'nameCriteria',)
    ordering = ('idCriteria',)




############################################################################### Category
class Category(models.Model):
    idCategory = models.AutoField(primary_key=True)
    nameCategory = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameCategory

    class Meta:
        managed = True
        db_table = "Category"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameCategory', 'status',)
    list_display = ('idCategory', 'nameCategory')
    list_display_links = ('idCategory', 'nameCategory')
    search_fields = ('idCategory', 'nameCategory',)
    ordering = ('idCategory',)




############################################################################### Polymer
class Polymer(models.Model):
    idPolymer = models.AutoField(primary_key=True)
    namePolymer = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.namePolymer

    class Meta:
        managed = True
        db_table = "Polymer"


@admin.register(Polymer)
class PolymerAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('namePolymer', 'status',)
    list_display = ('idPolymer', 'namePolymer')
    list_display_links = ('idPolymer', 'namePolymer')
    search_fields = ('idPolymer', 'namePolymer',)
    ordering = ('idPolymer',)




############################################################################### Motive
class Motive(models.Model):
    idMotive = models.AutoField(primary_key=True)
    nameMotive = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameMotive

    class Meta:
        managed = True
        db_table = "Motive"


@admin.register(Motive)
class MotiveAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameMotive', 'status',)
    list_display = ('idMotive', 'nameMotive')
    list_display_links = ('idMotive', 'nameMotive')
    search_fields = ('idMotive', 'nameMotive',)
    ordering = ('idMotive',)




############################################################################### Section
class Section(models.Model):
    idSection = models.AutoField(primary_key=True)
    nameSection = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameSection

    class Meta:
        managed = True
        db_table = "Section"


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameSection', 'status',)
    list_display = ('idSection', 'nameSection')
    list_display_links = ('idSection', 'nameSection')
    search_fields = ('idSection', 'nameSection',)
    ordering = ('idSection',)




############################################################################### SubSection
class SubSection(models.Model):
    idSubSection = models.AutoField(primary_key=True)
    nameSubSection = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.nameSubSection

    class Meta:
        managed = True
        db_table = "SubSection"


@admin.register(SubSection)
class SubSectionAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('nameSubSection', 'status',)
    list_display = ('idSubSection', 'nameSubSection')
    list_display_links = ('idSubSection', 'nameSubSection')
    search_fields = ('idSubSection', 'nameSubSection',)
    ordering = ('idSubSection',)




############################################################################### DrillBit
class DrillBit(models.Model):
    idDrillBit = models.AutoField(primary_key=True)
    codeDrillBit = models.CharField(max_length=250)
    status = models.CharField(max_length=3)
    regDate = models.DateTimeField(null=True, blank=True, auto_now_add=True, db_column='reg_date')
    regUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='reg_user')
    modDate = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='mod_date')
    modUser = models.CharField(max_length=30, null=True, blank=True, default="admin", db_column='mod_user')

    def __str__(self):
        return self.codeDrillBit

    class Meta:
        managed = True
        db_table = "DrillBit"


@admin.register(DrillBit)
class DrillBitAdmin(admin.ModelAdmin):
    exclude = ['regDate', 'regUser', 'modDate', 'modUser']
    fields = ('codeDrillBit', 'status',)
    list_display = ('idDrillBit', 'codeDrillBit')
    list_display_links = ('idDrillBit', 'codeDrillBit')
    search_fields = ('idDrillBit', 'codeDrillBit',)
    ordering = ('idDrillBit',)
