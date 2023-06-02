from django import forms
from .models import TimeSlot

import datetime


ATTRS_FIELD = {"class": "input mb-4"}


class DateInput(forms.DateTimeInput):
    input_type = "datetime-local"


class TimeSlotForm(forms.Form):
    first_name = forms.ChoiceField(
        choices=TimeSlot.PEOPLE, widget=forms.Select(attrs=ATTRS_FIELD)
    )
    slot_type = forms.CharField(widget=forms.TextInput(attrs=ATTRS_FIELD))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs=ATTRS_FIELD))
    date_start = forms.DateTimeField(
        label="Starting date",
        widget=DateInput(attrs=ATTRS_FIELD),
    )

    date_end = forms.DateTimeField(
        label="Ending date",
        widget=DateInput(attrs=ATTRS_FIELD),
    )

    class Meta:
        model = TimeSlot
        # fields = "_all_" # pas nécessaire si spécifiés au-dessus
