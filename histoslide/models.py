from os.path import dirname

from django.db import models


class Slide(models.Model):
    SlideType_choices = (
        (2, 'openslide'),)
    Name = models.CharField(max_length=50)
    ScannedBy = models.CharField(max_length=50, blank=True)
    ScannedDate = models.DateField(blank=True)
    InsertedBy = models.CharField(max_length=50, blank=True)
    InsertedDate = models.DateField(blank=True)
    SlideType = models.IntegerField(choices=SlideType_choices)    
    UrlPath = models.CharField(max_length=200)

    class Meta:
        ordering = ['UrlPath']

    def __str__(self):
        return u'%s - %s' % (dirname(self.UrlPath), self.Name)


class SlideBookmark(models.Model):
    # A bookmark as retrieved from openseadragon, getCenter(), getZoom()
    Slide = models.ForeignKey(Slide, on_delete=models.CASCADE)
    Text = models.CharField(max_length=50)
    CenterX = models.FloatField(default=0.0)
    CenterY = models.FloatField(default=0.0)
    Zoom = models.FloatField(default=1.0)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        abstract = True

    def __str__(self):
        return self.Text


class SlideAnnotation(models.Model):
    Slide = models.ForeignKey(Slide, on_delete=models.CASCADE)
    AnnotationJSON = models.TextField()
    Length = models.FloatField()
    LengthUnit = models.CharField(max_length=10, blank=True)

    class Meta:
        abstract = True
