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


from django.urls import register_converter
from .converters import DateConverter


register_converter(DateConverter, "date")


from .views import give_time_slots, compare_time_slots

app_name = "slot"

urlpatterns = [
    path("give_time_slots", give_time_slots, name="give_time_slots"),
    path(
        "compare_time_slots/<date:date_from>/<date:date_to>",
        compare_time_slots,
        name="compare_time_slots",
    ),
]
