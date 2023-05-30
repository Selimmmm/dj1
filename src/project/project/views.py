from django.shortcuts import render
from django.http import HttpResponse


def squares(request):
    x = []
    for i in range(10):
        x.append(str(i**2))
    return HttpResponse(f"<p>{'<br>'.join(x)}</p>")


def compute_squares(request, number):
    numbers = list(range(number))
    squares = [n**2 for n in numbers]
    context = {"squares": squares, "numbers": numbers}
    return render(request, "compute_squares.html", context=context)
