from django.db import models

SOURCES = (
    ('Raid', 'Raid'),
    ('Dungeon', 'Dungeon'),
)
SLOTS = (
    ('Head', 'Head'),
    ('Shoulder', 'Shoulder'),
    ('Back', 'Back'),
    ('Chest', 'Chest'),
    ('Wrist', 'Wrist'),
    ('Hands', 'Hands'),
    ('Waist', 'Waist'),
    ('Legs', 'Legs'),
    ('Feet', 'Feet')
)
OTHERSLOTS = (
    ('Neck', 'Neck'),
    ('Finger', 'Finger'),
)
SPECS = (
    ('Heal', 'Heal'),
    ('Tank', 'Tank'),
    ('Caster', 'Caster'),
    ('Melee', 'Melee'),
)


class Cloth(models.Model):
    slot = models.CharField(max_length=10, choices=SLOTS)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=7, choices=SOURCES)
    source_name = models.CharField(max_length=25)
    strength = models.BooleanField(default=False)
    agility = models.BooleanField(default=False)
    intellect = models.BooleanField(default=True)
    haste = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    vers = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    image_url = models.CharField(max_length=250)
    wowhead_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Leather(models.Model):
    slot = models.CharField(max_length=10, choices=SLOTS)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=7, choices=SOURCES)
    source_name = models.CharField(max_length=25)
    strength = models.BooleanField(default=False)
    agility = models.BooleanField()
    intellect = models.BooleanField()
    haste = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    vers = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    image_url = models.CharField(max_length=250)
    wowhead_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Mail(models.Model):
    slot = models.CharField(max_length=10, choices=SLOTS)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=7, choices=SOURCES)
    source_name = models.CharField(max_length=25)
    strength = models.BooleanField(default=False)
    agility = models.BooleanField()
    intellect = models.BooleanField()
    haste = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    vers = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    image_url = models.CharField(max_length=250)
    wowhead_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Plate(models.Model):
    slot = models.CharField(max_length=10, choices=SLOTS)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=7, choices=SOURCES)
    source_name = models.CharField(max_length=25)
    strength = models.BooleanField()
    agility = models.BooleanField()
    intellect = models.BooleanField()
    haste = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    vers = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    image_url = models.CharField(max_length=250)
    wowhead_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Other(models.Model):
    slot = models.CharField(max_length=10, choices=OTHERSLOTS)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=7, choices=SOURCES)
    source_name = models.CharField(max_length=25)
    haste = models.IntegerField(default=0)
    crit = models.IntegerField(default=0)
    vers = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    image_url = models.CharField(max_length=250)
    wowhead_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Trinket(models.Model):
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=7, choices=SOURCES)
    source_name = models.CharField(max_length=25)
    spec = models.CharField(max_length=10, choices=SPECS)
    image_url = models.CharField(max_length=250)
    wowhead_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name
