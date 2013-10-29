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

class Location(Subrecord, TaggedSubrecordMixin):
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
    drug = ForeignKeyOrFreeText(option_models['drug'])
    dose = models.CharField(max_length=255, blank=True)
    route = ForeignKeyOrFreeText(option_models['drug_route'])
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Problems(Subrecord):
    condition = ForeignKeyOrFreeText(option_models['condition'])
    provisional = models.BooleanField()
    details = models.CharField(max_length=255, blank=True)
    date_of_diagnosis = models.DateField(blank=True, null=True)
