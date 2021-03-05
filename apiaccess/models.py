from django.db import models


class AccessToken(models.Model):
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
