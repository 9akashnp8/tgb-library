from django.core.management.base import BaseCommand
from library.models import Author, Book, Country

import csv

class Command(BaseCommand):
    """
    Custom Management Command to Import Authors
    into the database via a csv file
    """
    help = 'Import Authors into TGB Library via a csv file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='This is the csv file name (without.csv extension) to be imported')

    def handle(self, *args, **kwargs):
        filename = kwargs['file']
        if filename is not None:
            with open(f"{filename}.csv", encoding='utf8') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    author_name = row[0]
                    author_age = row[1]
                    author_gender = row[2]
                    country_iso3 = row[3]
                    try:
                        author = Author.objects.get(name=author_name)
                        self.stdout.write(self.style.WARNING(f"{author.name} Already Exists, Skipping."))
                    except Author.DoesNotExist:
                        try:
                            country = Country.objects.get(iso3=country_iso3)
                            new_author = Author.objects.create(
                                name=author_name,
                                age=author_age,
                                gender=author_gender,
                                country=country
                            )
                            self.stdout.write(self.style.SUCCESS(f"Imported {new_author.name}"))
                        except Country.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f"Country: {country.iso3} Does Not Exist, Please Validate the ISO3 Code."))
                self.stdout.write(self.style.SUCCESS(f"Import Complete"))