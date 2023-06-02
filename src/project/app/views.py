from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


import base64
from secrets import token_urlsafe
import requests
from bs4 import BeautifulSoup

import logging

logger = logging.getLogger(__name__)


from .models import Prospect

# Create your views here.


def index(request):
    """Example view."""
    # return HttpResponse(f"Hi")
    return render(request, "index.html")


def compute_square(request, number):
    """Example view with context and url parameter and templating"""
    square = number * number
    context = {"square": square, "number": number}
    return render(request, "compute_square.html", context=context)


def compute_squares(request, number):
    """Example view with context and url parameter + more complex templating"""
    numbers = list(range(number))
    squares = [n**2 for n in numbers]
    context = {
        "number_and_square": [
            {"number": number, "square": square}
            for number, square in zip(numbers, squares)
        ]
    }
    return render(request, "compute_squares.html", context=context)


def random_wiki(request):
    """Dynamic view + scraping"""
    url = "https://en.wikipedia.org/wiki/Special:RandomInCategory/Featured_articles"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    language_list = soup.find_all("a", class_="interlanguage-link-target")
    language_list = [language.span.text for language in language_list]

    page_title = soup.find(id="firstHeading").text
    context = {
        "page_title": page_title,
        "languages": language_list,
    }
    return render(request, "random_wiki.html", context=context)


def bulma_front(request):
    """Bulma Example"""
    return render(request, "bulma/main.html")


def send_image(request, data):
    """Get image from URL."""
    codex = data.split("data:image/")
    if len(codex) == 1:
        codex = "jpeg"
        base64_image = data
    else:
        codex = codex[1].split(";")[0]
        base64_image = data.split(f"data:image/{codex};base64,")[1]

    img = base64.b64decode(base64_image)
    with open(f"./src/project/upload/{token_urlsafe(16)}.{codex}", "wb") as f:
        f.write(img)

    context = {"codex": codex, "base64_image": base64_image}
    return render(request, "send_image.html", context=context)


from .validation import validate_data


@require_http_methods(["GET", "POST"])
def form_prospect(request):
    """Form example."""
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        tel = request.POST.get("tel")
        email = request.POST.get("email")
        message = request.POST.get("message")

        validation = validate_data(first_name, last_name, tel, email, message)

        if all(validation.values()):
            prospect_object = Prospect.objects.create(
                first_name=first_name,
                last_name=last_name,
                tel=tel,
                email=email,
                message=message,
            )
            prospect_object.save()

            return render(request, "form_received.html")

        else:
            return render(
                request,
                "form_prospect.html",
                context={
                    "validation": validation,
                    "tel": tel,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "message": message,
                },
            )

    return render(request, "form_prospect.html", context={})


from django.contrib.auth.decorators import login_required


@login_required
def hello_user(request):
    """Redirect to this page after login. See settings.py LOGIN_REDIRECT_URL."""
    return render(request, "hello_user.html", context={})
