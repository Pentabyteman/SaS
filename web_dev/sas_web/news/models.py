from django.db import models


# Create your models here.
class ParteiWerbung(models.Model):
    partei = models.ForeignKey('meingoethopia.Partei')
    image = models.ImageField('Bild', upload_to='partei_bilder')
    wahlprogramm = models.TextField('Wahlprogramm')

    @property
    def url(self):
        return "/wahl/partei/{}".format(self.pk)

    def __str__(self):
        return str(self.partei)

    class Meta:
        verbose_name = 'Parteiwerbung'
        verbose_name_plural = 'Parteienwerbung'


class ParteiAnhang(models.Model):
    name = models.CharField('Name', max_length=100)
    data = models.FileField('Datei')
    partei = models.ForeignKey(ParteiWerbung)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Anhang'
        verbose_name_plural = 'Anhänge'


class PraesidentWerbung(models.Model):
    praesident = models.ForeignKey('meingoethopia.PresidentCandidate')
    image = models.ImageField('Bild', upload_to='praesident_bilder')
    wahlprogramm = models.TextField('Wahlprogramm')

    @property
    def url(self):
        return "/wahl/praesident/{}".format(self.pk)

    def __str__(self):
        return str(self.praesident)

    class Meta:
        verbose_name = 'Präsidentwerbung'
        verbose_name_plural = 'Präsidentenwerbung'


class PraesidentAnhang(models.Model):
    name = models.CharField('Name', max_length=100)
    data = models.FileField('Datei')
    praesident = models.ForeignKey(PraesidentWerbung)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Anhang'
        verbose_name_plural = 'Anhänge'
