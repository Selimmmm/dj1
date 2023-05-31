"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path


from .views import index
from .views import compute_square
from .views import compute_squares
from .views import bulma_front
from .views import random_wiki
from .views import send_image
from .views import form_prospect

urlpatterns = [
    path("", index, name="index"),
    path("compute_square/<int:number>", compute_square, name="compute_square"),
    path("compute_squares/<int:number>", compute_squares, name="compute_squares"),
    path("bulma_front", bulma_front, name="bulma_front"),
    path("random_wiki", random_wiki, name="random_wiki"),
    re_path(r"^send_image/(P?<data>.+)", send_image, name="send_image"),
    path("form_prospect", form_prospect, name="form_prospect"),
]
