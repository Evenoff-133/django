from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run BBC News Crawler'

    def handle(self, *args, **options):
        pass
