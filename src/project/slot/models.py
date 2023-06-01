from django.db import models
from django.db.models import Model


class TimeSlot(Model):
    JEAN = "JEAN"
    JEANNE = "JEANNE"
    JOHN = "JOHN"

    PEOPLE = [
        (JEAN, "JEAN"),
        (JEANNE, "JEANNE"),
        (JOHN, "JOHN"),
    ]

    first_name = models.CharField(
        choices=PEOPLE, blank=False, null=False, max_length=255
    )

    slot_type = models.CharField(blank=False, null=False, max_length=255)
    message = models.TextField(blank=False, null=False)
    date_start = models.DateTimeField(blank=False, null=False)
    date_end = models.DateTimeField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
