from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    test = models.BigIntegerField(null=True, blank=True,)
    testdata = models.IntegerField(null=True, blank=True,)
    test1 = models.TimeField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Test1(models.Model):
    "Generated Model"
    test = models.IntegerField()
