from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Brand(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(null=False, choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):

    class Type(models.TextChoices):
        Records = 'RCD'
        Clothing = 'CLT'
        Posters = 'PST'
        Miscellaneous = 'MSN'

    title =  models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(max_length=5)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
