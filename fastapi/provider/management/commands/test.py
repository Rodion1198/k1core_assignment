from django.core.management import BaseCommand

from block.tasks import fetch_latest_block


class Command(BaseCommand):

    def handle(self, *args, **options):
        fetch_latest_block()
