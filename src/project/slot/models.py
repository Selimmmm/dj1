from django.db import models
from django.db.models import Model


import operator
import itertools


class PerUserManager(models.Manager):
    def grouped(self, date_from, date_to):
        # Get timeslots
        timeslots = (
            super(PerUserManager, self)
            .get_queryset()
            .filter(date_start__gte=date_from, date_end__lte=date_to)
            .values("date_start", "date_end", "first_name", "slot_type")
        )

        # Group this way : {user_a: [ts1, ts2, ts3...], user_b: ...}
        timeslots_per_user = {}
        for first_name, timeslots in itertools.groupby(
            timeslots, key=operator.itemgetter("first_name")
        ):
            timeslots = list(timeslots)

            # Compute the % start and length
            for ts in timeslots:
                full_period_seconds = (date_to - date_from).total_seconds()

                # the progress will start at
                ts["percent_start"] = round(
                    100
                    * (
                        ts["date_start"].replace(tzinfo=None) - date_from
                    ).total_seconds()
                    / full_period_seconds,
                    2,
                )
                # the progress will have a length of
                ts["percent_length"] = round(
                    100
                    * (ts["date_end"] - ts["date_start"]).total_seconds()
                    / full_period_seconds,
                    2,
                )
            timeslots_per_user[first_name] = timeslots
        return timeslots_per_user


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

    per_user = PerUserManager()
