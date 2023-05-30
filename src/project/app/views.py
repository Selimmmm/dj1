from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
    # return HttpResponse(f"Hi")
    return render(request, "index.html")


def compute_square(request, number):
    square = number * number
    context = {"square": square, "number": number}
    return render(request, "compute_square.html", context=context)


def compute_squares(request, number):
    numbers = list(range(number))
    squares = [n**2 for n in numbers]
    context = {
        "number_and_square": [
            {"number": number, "square": square}
            for number, square in zip(numbers, squares)
        ]
    }
    return render(request, "compute_squares.html", context=context)
