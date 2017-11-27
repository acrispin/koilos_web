from rest_framework.serializers import ModelSerializer
from .models import State, Category, Criteria, DrillBit, Motive, Polymer, Section, SubSection


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('idState', 'nameState', 'status',)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('idCategory', 'nameCategory', 'status',)


class CriteriaSerializer(ModelSerializer):
    class Meta:
        model = Criteria
        fields = ('idCriteria', 'nameCriteria', 'status',)


class DrillBitSerializer(ModelSerializer):
    class Meta:
        model = DrillBit
        fields = ('idDrillBit', 'codeDrillBit', 'status',)


class MotiveSerializer(ModelSerializer):
    class Meta:
        model = Motive
        fields = ('idMotive', 'nameMotive', 'status',)


class PolymerSerializer(ModelSerializer):
    class Meta:
        model = Polymer
        fields = ('idPolymer', 'namePolymer', 'status',)


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ('idSection', 'nameSection', 'status',)


class SubSectionSerializer(ModelSerializer):
    class Meta:
        model = SubSection
        fields = ('idSubSection', 'nameSubSection', 'status',)