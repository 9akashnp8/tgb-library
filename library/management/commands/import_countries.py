from django.core.management.base import BaseCommand
from library.models import Author, Book, Country

import csv

class Command(BaseCommand):
    help = 'Import Countries into TGB Library via a csv file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='This is the csv file name (without.csv extension) to be imported')

    def handle(self, *args, **kwargs):
        filename = kwargs['file']
        if filename is not None:
            with open(f"{filename}.csv", encoding='utf8') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    name = row[0]
                    iso = row[1]
                    iso3 = row[2]
                    country = Country.objects.create(
                        iso=iso,
                        iso3=iso3,
                        name=name
                    )
                    self.stdout.write("Created %s" % name)