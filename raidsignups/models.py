from django.db import models
import string
import random
# Create your models here.


def generate_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if Raid.objects.filter(code=code).count() == 0:
            return code


class Raid(models.Model):
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Raider(models.Model):
    name = models.CharField(max_length=20)
    playerclass = models.CharField(max_length=20)
    playerspec = models.CharField(max_length=20)
    latestraid = models.ForeignKey(Raid, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
