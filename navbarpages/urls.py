from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("itemfinder/", views.itemfinder, name="itemfinder"),
    path("result/", views.result, name="result"),
    path("dungeoncheck/", views.dungeoncheck, name="dungeoncheck")
]
