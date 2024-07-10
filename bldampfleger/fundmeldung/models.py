from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fundmeldung(models.Model):
    fundzeit = models.DateField(auto_now_add=True)
    gemarkung = models.CharField(max_length=100, null=True)
    landkreis = models.CharField(max_length=100, null=True)
    fundplatznummer = models.IntegerField(blank=True, null=True)
    flurname = models.CharField(max_length=100, blank=True, null=True)
    flur = models.IntegerField(null=True)
    flurstück = models.IntegerField(null=True)
    strassenummer = models.CharField(max_length=100, blank=True, null=True)
    koordinatensystem = models.CharField(max_length=100, null=True)
    utm_zone = models.CharField(max_length=100, null=True)
    eckpunkt1_nord = models.CharField(max_length=100, null=True)
    eckpunkt1_ost = models.CharField(max_length=100, null=True)
    eckpunkt2_nord = models.CharField(max_length=100, null=True)
    eckpunkt2_ost = models.CharField(max_length=100, null=True)
    eckpunkt3_nord = models.CharField(max_length=100, null=True)
    eckpunkt3_ost = models.CharField(max_length=100, null=True)
    eckpunkt4_nord = models.CharField(max_length=100, null=True)
    eckpunkt5_ost = models.CharField(max_length=100, null=True)
    einmessungsart = models.CharField(max_length=100, null=True)
    lagezumortskern_meter = models.IntegerField(null=True,blank=True)
    lagezumortskern = models.CharField(max_length=100, null=True)
    lageimgelaende = models.CharField(max_length=30, blank=True, null=True)
    class LageimGelaende(models.TextChoices):
        hoehenlage =  "1", "Höhenlage"
        niederung =  "2", "Niederung"
        hang =  "3", "Hang (abfallend nach ...)"
        ebene =  "4",  "Ebene"
        amseefluss =  "5", "am See/Fluss..."
        imseefluss =  "6", "im See/Fluss"
    lageimgelaende = models.CharField(
        max_length=1,
        choices=LageimGelaende.choices,
        default=LageimGelaende.ebene
    )
    ergenzungLiG = models.CharField(max_length=30, blank=True, null=True)
    #gelaendenutzung = models.CharField(max_length=30, blank=True, null=True)
    class Gelaendenutzung(models.TextChoices):
        strasse =  "1", "Straße/Weg/Platz"
        acker =  "2", "Acker"
        garten =  "3", "Garten"
        grube =  "4",  "Grube"
        wiese =  "5", "Wiese"
        grundstueck =  "6", "bebautes Grundstück"
        oedland =  "7",  "Ödland"
        wald =  "8", "Wald"
        moor =  "9", "Moor"
        gewaesser =  "10", "Gewässer"
    gelaendenutzung = models.CharField(
        max_length=2,
        choices=Gelaendenutzung.choices,
        default=Gelaendenutzung.acker
    )
    #bodenart = models.CharField(max_length=30, blank=True, null=True)
    class Bodenart(models.TextChoices):
        sand =  "1", "Sand"
        lehm =  "2", "Lehm"
        ton =  "3", "Ton"
        mergel =  "4",  "Mergel"
        lehmigersand =  "5", "lehmiger Sand"
        torf =  "6", "Torf"
    bodenart = models.CharField(
        max_length=1,
        choices=Bodenart.choices,
        default=Bodenart.sand
    )
    befundart = models.CharField(max_length=30, blank=True, null=True)
    zeitstellung = models.CharField(max_length=30, blank=True, null=True)
    kultur = models.CharField(max_length=30, blank=True, null=True)
    gruppe = models.CharField(max_length=30, blank=True, null=True)
    auffindungsart = models.CharField(max_length=30, blank=True, null=True)
    erhaltuungszustand = models.TextField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.gemarkung
    
class Linksammlung(models.Model):
    name = models.CharField(max_length=100, null=True)
    url = models.URLField()
    beschreibung = models.TextField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.name
    
class Pfleger(models.Model):
    benutzer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)
    
def Lageimgelaende():
    lageimgelaende = ["Höhenlage", "Niederung", "Hang (abfallend nach ...)",  "Ebene", "am See/Fluss...", "im See/Fluss"]
    return lageimgelaende