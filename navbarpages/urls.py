from django.urls import path
from . import views

urlpatterns=[
    path("",views.homepage,name="homepage"),
    path("itemfinder/",views.itemfinder,name="itemfinder"),
]