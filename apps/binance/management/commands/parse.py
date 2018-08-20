from django.core.management.base import BaseCommand
from apps.binance._parse import run


class Command(BaseCommand):

    help = 'Parse data into specific table'

    def handle(self, *args, **options):
        try:
            # Parse data into specific table
            run()
        except Exception as ex:
            self.stdout.write('Parse data process has not been completed, there is an error: {0}'.format(ex))
