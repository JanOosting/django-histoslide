from os import walk, path
from datetime import date

from django.contrib import admin
from django.conf import settings

from .models import Slide


class SlideAdmin(admin.ModelAdmin):
    actions = ['add_new_slides']
    
    def add_new_slides(self, request, queryset):
        # Collect all new slide files in the media dir
        currentuser = request.user.username
        for root, dirs, files in walk(path.join(settings.HISTOSLIDE_SLIDEROOT)):
            for slide_file in files:
                if slide_file.lower().endswith(settings.SLIDEFILE_EXTENSIONS):
                    urlnew = path.join(path.relpath(root, settings.HISTOSLIDE_SLIDEROOT), slide_file)
                    # only include slides that are not in the slide list yet
                    try:
                        slide = Slide.objects.get(UrlPath=urlnew)
                    except Slide.DoesNotExist:
                        slide = Slide(Name=path.splitext(slide_file)[0], ScannedBy=currentuser,
                                      ScannedDate=date.today(), InsertedBy=currentuser, InsertedDate=date.today(),
                                      SlideType=2, UrlPath=urlnew)
                        slide.save()


admin.site.register(Slide, SlideAdmin)
