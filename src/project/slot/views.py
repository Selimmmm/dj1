from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from .form import TimeSlotForm

from .models import TimeSlot


@require_http_methods(["GET", "POST"])
def give_time_slots(request):
    """Form view for getting the Time Slots

    Args:
        request: django stuff

    Returns:
        render

    Info:
        ** -> de passer les arguments en tant que dictionnaire
        {"arg1": "bonjour", "arg2": "aurevoir"} ->
        ----> arg1="bonjour", arg2="aurevoir"
    """

    if request.method == "POST":
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            time_slot_inst = TimeSlot.objects.create(**form.cleaned_data)
            time_slot_inst.save()
        return render(request, "form_received.html")

    # Request can only be a GET
    form = TimeSlotForm()
    context = {"form": form}
    return render(request, "slots/give_time_slots.html", context=context)


def compare_time_slots(request, date_from, date_to):
    context = {"date_from": date_from, "date_to": date_to}
    print(date_from), print(date_to)
    return render(request, "slots/compare_time_slots.html", context=context)
