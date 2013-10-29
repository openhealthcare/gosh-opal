"""
List and detail view schema for GOSH-OPAL!
"""

from gosh import models

list_columns = [
    models.Location,
    models.Demographics,
    models.Treatment,
    models.Problem,
    models.Test,
    models.Task,
    models.Contact
    ]

detail_columns = [
    models.Location,
    models.Demographics,
    models.Treatment,
    models.Problem,
    models.Test,
    models.Task,
    models.Contact
    ]
