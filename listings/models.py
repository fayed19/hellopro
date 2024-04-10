from django.db import models

class Brand(models.Model):
    name = models.fields.CharField(max_length=100)


class Listing(models.Model):
    title =  models.fields.CharField(max_length=100)

