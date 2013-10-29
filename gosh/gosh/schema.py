"""
List and detail view schema for GOSH-OPAL!
"""

from gosh import models

list_columns = [
    models.Location,
    models.Demographics,
    models.Treatment,
    models.Problems
    ]

detail_columns = [
    models.Location,
    models.Demographics,
    models.Treatment,
    models.Problems
    ]
