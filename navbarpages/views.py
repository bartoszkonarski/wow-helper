from django.shortcuts import render
from itemfinder.models import Cloth, Leather, Mail, Plate, Trinket, Other
from django.db import models
import requests
import urllib
from django import template
# Create your views here.


def create_access_token(client_id, client_secret, region='us'):
    data = {'grant_type': 'client_credentials'}
    response = requests.post('https://%s.battle.net/oauth/token' %
                             region, data=data, auth=(client_id, client_secret))
    return response.json()


def homepage(response):
    return render(response, "home.html", {})


def itemfinder(response):
    return render(response, "finder.html", {})


def result(response):
    if response.method == "POST":
        itemtype = response.POST.get("itemtype")
        types = {"Cloth": Cloth,
                 "Leather": Leather,
                 "Mail": Mail,
                 "Plate": Plate,
                 "Cloak/Neck/Ring": Other,
                 "Trinket": Trinket}
        currentModel = types.get(itemtype)

        if len(response.POST.getlist("source[]")) == 2:
            q = currentModel.objects.all()
        elif response.POST.getlist("source[]")[0] == "raid":
            q = currentModel.objects.filter(source="Raid")
        else:
            q = currentModel.objects.filter(source="Dungeon")

        armortypes = [Cloth, Leather, Mail, Plate]
        offstats = response.POST.getlist('offstat[]')
        if currentModel in armortypes:
            if response.POST.get('mainstat') == "Intellect":
                q = q.filter(intellect=True)
            elif response.POST.get('mainstat') == "Agility":
                q = q.filter(agility=True)
            else:
                q = q.filter(strength=True)
        elif currentModel == Other:
            if "Mastery" in offstats:
                q = q.filter(mastery__gt=0)
            if "Vers" in offstats:
                q = q.filter(vers__gt=0)
            if "Crit" in offstats:
                q = q.filter(crit__gt=0)
            if "Haste" in offstats:
                q = q.filter(haste__gt=0)
        else:
            trinket_spec = response.POST.get('spec')
            q = q.filter(spec=trinket_spec)
        if currentModel in armortypes:
            if "Mastery" in offstats:
                q = q.filter(mastery__gt=0)
            if "Vers" in offstats:
                q = q.filter(vers__gt=0)
            if "Crit" in offstats:
                q = q.filter(crit__gt=0)
            if "Haste" in offstats:
                q = q.filter(haste__gt=0)

    return render(response, "result.html", {'objects': q, })

register = template.Library()

@register.filter
def get_encoded_dict(data_dict):
    return urllib.parse.urlencode(data_dict)

def dungeoncheck(response):

    access = create_access_token(
        "d7de467d23d148de8323181b37f03941", "wZ9mfpIsyQ3HznAv5sNYuYxaejoVadoJ")
    token = access['access_token']
    url = f"https://eu.api.blizzard.com/data/wow/guild/burning-legion/homeless/roster?namespace=profile-eu&locale=en_US&access_token={token}"

    apiresponse = requests.get(url).json()
    members = []
    for member in apiresponse['members']:
        if member['rank'] in (0, 1, 4, 5):
            members.append(member['character']['name'])
    members.remove('Cptcookie')
    members.append('Laykop')
    members_dict = {}

    for member in members:
        counter = 0
        url = f"https://raider.io/api/v1/characters/profile?region=eu&realm=Burning%20Legion&name={member}&fields=mythic_plus_weekly_highest_level_runs"
        apiresponse = requests.get(url).json()
        for key in apiresponse['mythic_plus_weekly_highest_level_runs']:
            if key['mythic_level'] >= 14:
                counter += 1
        members_dict[member] = counter

    sorted_dict = dict(sorted(members_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    return render(response, "dungeoncheck.html", {'sorted_dict':sorted_dict})
