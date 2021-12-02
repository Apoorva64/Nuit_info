from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RescuedBoat(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    id_plate = models.CharField(max_length=100, verbose_name=_('id_plate'), null=True)

    def __str__(self):
        return self.name


class RescueBoat(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    id_plate = models.CharField(max_length=100, verbose_name=_('id plate'), null=True)
    start_date = models.DateTimeField(verbose_name=_('start date'), null=True)

    def __str__(self):
        return self.name


class MedalOfHonor(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(max_length=1000, verbose_name=_("description"), null=True)
    img = models.ImageField(null=True)


    def __str__(self):
        return self.name


class Rescuer(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    first_name = models.CharField(max_length=100, verbose_name=_("first name"))
    last_name = models.CharField(max_length=100, verbose_name=_("last name"))
    description = models.TextField(max_length=1000, verbose_name=_("description"), null=True)
    medals = models.ManyToManyField(MedalOfHonor, verbose_name=_("medals of honor"), null=True)
    birth_date = models.DateTimeField(verbose_name=_("birth date"), null=True)
    death_date = models.DateTimeField(verbose_name=_("death date"), null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Rescue(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    rescue_boats = models.ManyToManyField(RescueBoat, verbose_name=_("rescue boats"))
    rescued_boats = models.ManyToManyField(RescuedBoat, verbose_name=_("rescued boats"), null=True)
    rescuers = models.ManyToManyField(Rescuer, verbose_name=_('rescuers'), null=True)
    rescue_date = models.DateTimeField(verbose_name=_("rescue date"))
    number_of_saved_people = models.IntegerField(verbose_name=_("number of saved people"), null=True)
    description = models.TextField(verbose_name=_("description"), null=True)

    def __str__(self):
        return self.description


class User(AbstractUser):
    # telephone = models.CharField(max_length=30)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class RescueStation(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(verbose_name=_("description"), null=True)
    latitude = models.FloatField(verbose_name=_("latitude"), null=True)
    longitude = models.FloatField(verbose_name=_("longitude"), null=True)
    rescuers = models.ManyToManyField(Rescuer, verbose_name=_("rescuers"), null=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    content = models.TextField(verbose_name=_("quote content"))
    rescue = models.ForeignKey(Rescue, verbose_name=_("rescue"), on_delete=models.SET_NULL, null=True)
    rescuer = models.ForeignKey(Rescuer, verbose_name=_("rescuer"), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.rescuer.first_name + " " + self.rescuer.last_name


ART_TYPE_CHOICES = (("book", _("book")),
                    ("boat", _("boat")),
                    ("painting", _("painting")),
                    )


class Art(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=300, choices=ART_TYPE_CHOICES, verbose_name=_("type"))
    creation_date = models.DateTimeField(verbose_name=_("creation date"), null=True)
    description = models.TextField(verbose_name=_("description"), null=True)
    editor_name = models.CharField(max_length=100, verbose_name=_("editor name"), null=True)
    name = models.CharField(max_length=100, verbose_name=_("name"))
    img = models.ImageField(null=True)

    def __str__(self):
        return self.name
