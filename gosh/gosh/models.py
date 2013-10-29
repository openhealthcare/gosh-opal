"""
GOSH-OPAL! implementation specific models
"""
from django.db import models

from opal.models import Subrecord, TaggedSubrecordMixin, option_models
from opal.utils.fields import ForeignKeyOrFreeText

__all__ = [
    'Location',
    'Demographics',
    'Treatment',
    'Problems',
    ]

class Location(TaggedSubrecordMixin, Subrecord):
    _is_singleton = True

    ward = models.CharField(max_length=255, blank=True)
    bed = models.CharField(max_length=255, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)
    # TODO rename to date_of_discharge?
    discharge_date = models.DateField(null=True, blank=True)


class Demographics(Subrecord):
    _title = 'Name/DOB/Hosp'
    _is_singleton = True

    name = models.CharField(max_length=255, blank=True)
    hospital_number = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


class Treatment(Subrecord):
    _title = 'Diagnosis / Treatment'

    condition = ForeignKeyOrFreeText(option_models['condition']) # AML
    details = models.CharField(max_length=255, blank=True) # M6 t(11,19)
    provisional = models.BooleanField()
    date_of_diagnosis = models.DateField(blank=True, null=True)

    drug = ForeignKeyOrFreeText(option_models['drug'])
    dose = models.CharField(max_length=255, blank=True)
    route = ForeignKeyOrFreeText(option_models['drug_route'])
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Problem(Subrecord):
    _title = 'Problems'

    condition = ForeignKeyOrFreeText(option_models['condition'])
    provisional = models.BooleanField()
    details = models.CharField(max_length=255, blank=True)
    date_of_diagnosis = models.DateField(blank=True, null=True)


class Test(Subrecord):
    _title = 'Investigations/Results'

    test = models.CharField(max_length=255)
    date_ordered = models.DateField(null=True, blank=True)
    details = models.CharField(max_length=255, blank=True)
    result = models.CharField(max_length=200, blank=True)


class Task(Subrecord):
    _title = 'Tasks'

    name = models.CharField(max_length=255, blank=True)
    completed = models.BooleanField(default=False)


class Contact(Subrecord):
    contact_details = models.CharField(max_length=255, blank=True)
    contact_name = models.CharField(max_length=255, blank=True)
