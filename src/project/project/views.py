from django.shortcuts import render
from django.http import HttpResponse


def squares(request):
    """First view example. Don't put them outside of apps like this one :)"""
    x = []
    for i in range(10):
        x.append(str(i**2))
    return HttpResponse(f"<p>{'<br>'.join(x)}</p>")
