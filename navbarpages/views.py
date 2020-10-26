from django.shortcuts import render
from itemfinder.models import Cloth,Leather,Mail,Plate,Trinket,Other
from django.db import models
# Create your views here.
def homepage(response):
    return render(response,"home.html",{})

def itemfinder(response):
    return render(response,"finder.html",{})

def result(response):
    if response.method == "POST":
        itemtype = response.POST.get("itemtype")
        print(itemtype)
        types = {"Cloth": Cloth,
               "Leather": Leather,
               "Mail": Mail,
               "Plate": Plate,
               "Neck/Ring": Other,
               "Trinket": Trinket}
        currentModel = types.get(itemtype)
        print(currentModel)
        q = currentModel.objects.all()
        for item in q:
            print(item)

    return render(response,"result.html",{})
