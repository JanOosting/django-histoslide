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
        ordering = ['Name']

    def __unicode__(self):
        return self.Name
