from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def give_time_slots(request):
    if request.method == "POST":
        pass
    context = {}
    return render(request, "slots/give_time_slots.html", context=context)
