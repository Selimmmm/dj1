from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from .form import TimeSlotForm


@require_http_methods(["GET", "POST"])
def give_time_slots(request):
    if request.method == "POST":
        pass

    form = TimeSlotForm()
    context = {"form": form}
    return render(request, "slots/give_time_slots.html", context=context)
