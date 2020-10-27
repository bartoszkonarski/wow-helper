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
        types = {"Cloth": Cloth,
               "Leather": Leather,
               "Mail": Mail,
               "Plate": Plate,
               "Neck/Ring": Other,
               "Trinket": Trinket}
        currentModel = types.get(itemtype)
        print(response.POST)
        print(response.POST.getlist('source[]'))
        print(response.POST.getlist("source[]")[0])
        if len(response.POST.getlist("source[]")) == 2:
            q = currentModel.objects.all()
        elif response.POST.getlist("source[]")[0] == "raid":
            q = currentModel.objects.filter(source="Raid")
        else:
            q = currentModel.objects.filter(source="Dungeon")
        armortypes = [Cloth,Leather,Mail,Plate]
        offstats = response.POST.getlist('offstat[]')
        print(offstats)
        if currentModel in armortypes:
            if response.POST.get('mainstat') == "Intellect":
                q = q.filter(intellect=True)
            elif response.POST.get('mainstat') == "Agility":
                q = q.filter(agility=True)
            else:
                q = q.filter(strength=True)
        elif currentModel == Other:
            if "Mastery" in offstats:
                q= q.filter(mastery__gt=0)
            if "Vers" in offstats:
                q= q.filter(vers__gt=0)
            if "Crit" in offstats:
                q= q.filter(crit__gt=0)
            if "Haste" in offstats:
                q= q.filter(haste__gt=0)
        else:
            trinket_spec = response.POST.get('spec')
            q = q.filter(spec=trinket_spec)
        if currentModel in armortypes:
            if "Mastery" in offstats:
                q= q.filter(mastery__gt=0)
            if "Vers" in offstats:
                q= q.filter(vers__gt=0)
            if "Crit" in offstats:
                q= q.filter(crit__gt=0)
            if "Haste" in offstats:
                q= q.filter(haste__gt=0)
        for item in q:
            print(item)

    return render(response,"result.html",{'objects': q,})
