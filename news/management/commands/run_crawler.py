from django.core.management.base import BaseCommand
from news.crawlers.bbc_crawler import run, crawl_one


class Command(BaseCommand):
    help = 'Run BBC News Crawler'

    def handle(self, *args, **options):
        run()