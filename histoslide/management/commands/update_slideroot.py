from django.core.management.base import BaseCommand
from histoslide.models import Slide

class Command(BaseCommand):
    path_prefix = 'slideobserver/media/'
    help = 'remove "%s" from Slides' % path_prefix

    def add_arguments(self, parser):
        parser.add_argument(
            '-t', '--test', action='store_true', dest='testing',
            help='Do not change database, but display number of affected slides',
        )

    def handle(self, *args, **options):
        qs = Slide.objects.filter(UrlPath__contains= self.path_prefix)
        print('%d slides containing "%s" were found' % (len(qs), self.path_prefix))
        if not options['testing']:
            for slide in qs:
                slide.UrlPath = slide.UrlPath.replace(self.path_prefix, '')
                slide.save()
