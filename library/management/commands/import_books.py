from django.core.management.base import BaseCommand
from library.models import Author, Book, Country

import csv

class Command(BaseCommand):
    """
    Custom Management Command to Import Books (& Unadded Authors)
    into the database via a csv file
    """
    help = 'Display something'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='This is the csv file name (without.csv extension) to be imported')

    def handle(self, *args, **kwargs):
        filename = kwargs['file']
        if filename is not None:
            with open(f"{filename}.csv", encoding='utf8') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    book_name = row[0]
                    date_of_publishing = row[1]
                    number_of_pages = row[2]
                    average_critics_rating = row[3]
                    author_name = row[4]
                    author_age = row[5]
                    author_gender = row[6]
                    country_iso3 = row[7]
                    try:
                        book = Book.objects.get(name=book_name)
                        self.stdout.write(f"{book.name} already exists, skipping.")
                        pass
                    except Book.DoesNotExist:
                        try:
                            country = Country.objects.get(iso3=country_iso3)
                            try:
                                author = Author.objects.get(name=author_name)
                                Book.objects.create(
                                    name=book_name,
                                    author=author,
                                    date_of_publishing=date_of_publishing,
                                    number_of_pages=number_of_pages,
                                    average_critics_rating=average_critics_rating
                                )
                            except Author.DoesNotExist:
                                self.stdout.write(f"{author_name}: Author Does Not Exist, Creating Author")
                                author = Author.objects.create(
                                    name=author_name,
                                    age=author_age,
                                    gender=author_gender,
                                    country=country
                                )
                                Book.objects.create(
                                    name=book_name,
                                    author=author,
                                    date_of_publishing=date_of_publishing,
                                    number_of_pages=number_of_pages,
                                    average_critics_rating=average_critics_rating
                                )
                        except Country.DoesNotExist:
                            self.stdout.write(f"break at {row}, Country Does Not Exist. Check if the iso3 code is valid.")
                            break
                self.stdout.write(f"Import Complete")