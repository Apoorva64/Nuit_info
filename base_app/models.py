from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RescuedBoat(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    id_plate = models.CharField(max_length=100, verbose_name=_('id_plate'))

    def __str__(self):
        return self.name


class RescueBoat(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    id_plate = models.CharField(max_length=100, verbose_name=_('id plate'))
    start_date = models.DateTimeField(verbose_name=_('start date'))

    def __str__(self):
        return self.name


class MedalOfHonor(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(max_length=1000, verbose_name=_("description"))

    def __str__(self):
        return self.name


class Rescuer(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    name = models.CharField(max_length=100, verbose_name=_("name"))
    surname = models.CharField(max_length=100, verbose_name=_("surname"))
    description = models.TextField(max_length=1000, verbose_name=_("description"))
    medals = models.ManyToManyField(MedalOfHonor, verbose_name=_("medals of honor"))
    birth_date = models.DateTimeField(verbose_name=_("birth date"))
    death_date = models.DateTimeField(verbose_name=_("death date"))

    def __str__(self):
        return self.name


class Rescue(models.Model):
    has_been_published = models.BooleanField(verbose_name=_("has been published"))
    rescue_boats = models.ManyToManyField(RescueBoat, verbose_name=_("rescue boats"))
    rescued_boats = models.ManyToManyField(RescuedBoat, verbose_name=_("rescued boats"))
    rescuers = models.ManyToManyField(Rescuer, verbose_name=_('rescuers'))
    rescue_date = models.DateTimeField(verbose_name=_("rescue date"))
    number_of_saved_people = models.IntegerField(verbose_name=_("number of saved people"))
    description = models.TextField(verbose_name=_("description"))

    def __str__(self):
        return self.description


class User(AbstractUser):
    # telephone = models.CharField(max_length=30)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class RescueStation(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(verbose_name=_("description"))
    latitude = models.FloatField(verbose_name=_("latitude"))
    longitude = models.FloatField(verbose_name=_("longitude"))
    rescuers = models.ManyToManyField(Rescuer, verbose_name=_("rescuers"))

    def __str__(self):
        return self.name


class Quote(models.Model):
    content = models.TextField(verbose_name=_("quote content"))
    rescue = models.ForeignKey(Rescue, verbose_name=_("rescue"), on_delete=models.SET_NULL, null=True)
    rescuer = models.ForeignKey(Rescuer, verbose_name=_("rescuer"), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.rescuer.name


ART_TYPE_CHOICES = (("book", _("book")),
                    ("boat", _("boat")),
                    ("painting", _("painting")),
                    )


class Art(models.Model):
    author = models.CharField(max_length=100, )
    type = models.CharField(max_length=300, choices=ART_TYPE_CHOICES, verbose_name=_("type"))
    creation_date = models.DateTimeField(verbose_name=_("creation date"))
    description = models.TextField(verbose_name=_("description"), null=True)
    editor_name = models.CharField(max_length=100, verbose_name=_("editor name"), null=True)
    name = models.CharField(max_length=100, verbose_name=_("name"))

    def __str__(self):
        return self.name
