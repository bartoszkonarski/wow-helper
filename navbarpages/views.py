from django.shortcuts import render
from itemfinder.models import Cloth, Leather, Mail, Plate, Trinket, Other
from django.db import models
import requests
from apiaccess.models import AccessToken
from datetime import datetime, timezone, timedelta
from raidsignups.models import Raid, Raider, generate_code
# Create your views here.


def homepage(response):
    return render(response, "home.html", {})


def itemfinder(response):
    return render(response, "finder.html", {})


def result(response):
    if response.method == "POST":
        itemtype = response.POST.get("itemtype")
        types = {
            "Cloth": Cloth,
            "Leather": Leather,
            "Mail": Mail,
            "Plate": Plate,
            "Neck/Finger/Cloak": Other,
            "Trinket": Trinket,
        }
        currentModel = types.get(itemtype)

        if len(response.POST.getlist("source[]")) == 2:
            q = currentModel.objects.all()
        elif response.POST.getlist("source[]")[0] == "raid":
            q = currentModel.objects.filter(source="Raid")
        else:
            q = currentModel.objects.filter(source="Dungeon")

        armortypes = [Cloth, Leather, Mail, Plate]
        offstats = response.POST.getlist("offstat[]")
        if currentModel in armortypes:
            if response.POST.get("mainstat") == "Intellect":
                q = q.filter(intellect=True)
            elif response.POST.get("mainstat") == "Agility":
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
            trinket_spec = response.POST.get("spec")
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

    return render(
        response,
        "result.html",
        {
            "objects": q,
        },
    )


def dungeoncheck(response):
    if response.method != "POST":
        originalGuildName = "Homeless"
        guildName = "homeless"
        ranks = (0, 1, 4, 5)
    else:
        originalGuildName = response.POST.get("guildname")
        guildName = originalGuildName.lower()
        originalGuildName = originalGuildName.title()
        guildName = guildName.replace(" ", "-")
        ranks = response.POST.getlist("ranks[]")
        for i in range(len(ranks)):
            ranks[i] = int(ranks[i])
    if (datetime.now(timezone.utc) - AccessToken.objects.filter(name="BlizzardAPI")[0].date).total_seconds() < 3400:
        token = AccessToken.objects.filter(name="BlizzardAPI")[0].token
    else:
        access = create_access_token(
            "d7de467d23d148de8323181b37f03941", "wZ9mfpIsyQ3HznAv5sNYuYxaejoVadoJ")
        token = access["access_token"]
        p = AccessToken.objects.filter(name="BlizzardAPI")[0]
        p.token = token
        p.save()
    try:
        url = f"https://eu.api.blizzard.com/data/wow/guild/burning-legion/{guildName}/roster?namespace=profile-eu&locale=en_US&access_token={token}"

        print(requests.get(url).status_code)
        apiresponse = requests.get(url).json()

        members = []
        for member in apiresponse["members"]:
            if member["rank"] in ranks and member["character"]["level"] == 60:
                members.append(member["character"]["name"])
        # members.append("Laykop")
        members_dict = {}

        for member in members:
            counter = 0
            url = f"https://raider.io/api/v1/characters/profile?region=eu&realm=Burning%20Legion&name={member}&fields=mythic_plus_weekly_highest_level_runs"
            apiresponse = requests.get(url).json()
            for key in apiresponse["mythic_plus_weekly_highest_level_runs"]:
                if key["mythic_level"] >= 14:
                    counter += 1
            members_dict[member] = counter

        sorted_dict = dict(
            sorted(members_dict.items(),
                   key=lambda item: item[1], reverse=True)
        )
        return render(response, "dungeoncheck.html", {"sorted_dict": sorted_dict, "GuildName": originalGuildName})
    except:
        return render(response, "dungeoncheck.html", {"GuildName": "Exception!!!"})


def create_access_token(client_id, client_secret, region="us"):
    data = {"grant_type": "client_credentials"}
    response = requests.post(
        "https://%s.battle.net/oauth/token" % region,
        data=data,
        auth=(client_id, client_secret),
    )
    return response.json()


def raidview(response, raid_code):
    raid = Raid.objects.filter(code=raid_code)
    if response.method == "POST":
        name = response.POST.get('name')
        newRaider = Raider(name=name, playerclass="c1",
                           playerspec="c2", latestraid=raid[0])
        newRaider.save()
    raiders = raid[0].raider_set.all()
    print(raiders)

    date = raid[0].date
    return render(response, "raidview.html", {"raid_code": raid_code, "date": date, "raiders": raiders})


def raidcreate(response):
    return render(response, "raidcreate.html", {})


def raidlist(response):
    if response.method == "POST":
        code = generate_code()
        newRaid = Raid(code=code)
        newRaid.save()
    else:
        code = False
    return render(response, "raidlist.html", {"code": code, 'raids': reversed(Raid.objects.all())})
