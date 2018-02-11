=====
Histoslide
=====

Histoslide is a Django app to show openslide images. It can use other 
OpenSeadragon or the Google Maps API to navigate the images.

Quick start
-----------

1. Install openslide http://openslide.org/ on your system

2. Add "histoslide" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'histoslide',
    ]
3. Configure histoslide in settings.py

SLIDEFILE_EXTENSIONS = ('.jpg', '.jpeg', '.mrxs', '.tif', '.tiff')
HISTOSLIDE_SLIDEROOT = <absolute path to root of slide files>

	
4. Include the histoslide URLconf in your project urls.py like this::

    url(r'^histoslide/', include('histoslide.urls')),
	
5. Run `python manage.py migrate` to create the histoslide models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to register one or more slides (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/histoslide/slide/1/ to view the first slide.