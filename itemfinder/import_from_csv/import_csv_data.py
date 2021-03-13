import os
import sys
sys.path.append("F:\Projects\Python\WoW-helper\wowhelper")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'wowhelper.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wowhelper.settings")
import django

django.setup()

import csv
from itemfinder.models import Cloth, Leather, Mail, Plate, Other, Trinket


def import_armor_into_model(model_name, model):
    with open('items_django_app_' + model_name + '.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        row_num = 0
        for row in reader:
            if row_num == 0:
                row_num += 1
            else:
                model.objects.create(slot=row[0],
                                     name=row[1],
                                     source=row[2],
                                     source_name=row[3],
                                     strength=bool(int(row[4])),
                                     agility=bool(int(row[5])),
                                     intellect=bool(int(row[6])),
                                     haste=int(row[7]),
                                     crit=int(row[8]),
                                     vers=int(row[9]),
                                     mastery=int(row[10]),
                                     image_url=row[11],
                                     wowhead_url=row[12]
                                     )


def import_others():
    with open('items_django_app_others.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        row_num = 0
        for row in reader:
            if row_num == 0:
                row_num += 1
            else:
                Other.objects.create(slot=row[0],
                                     name=row[1],
                                     source=row[2],
                                     source_name=row[3],
                                     haste=int(row[4]),
                                     crit=int(row[5]),
                                     vers=int(row[6]),
                                     mastery=int(row[7]),
                                     image_url=row[8],
                                     wowhead_url=row[9]
                                     )


def import_trinkets():
    with open('items_django_app_trinkets.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        row_num = 0
        for row in reader:
            if row_num == 0:
                row_num += 1
            else:
                Trinket.objects.create(slot=row[0],
                                       name=row[1],
                                       source=row[2],
                                       source_name=row[3],
                                       spec=row[4],
                                       image_url=row[5],
                                       wowhead_url=row[6]
                                       )


import_armor_into_model("cloth", Cloth)
# import_armor_into_model("leather", Leather)
# import_armor_into_model("mail", Mail)
# import_armor_into_model("plate", Plate)
# import_others()
# import_trinkets()
