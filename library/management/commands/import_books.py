from django.core.management.base import BaseCommand
from library.models import Author, Book, Country

import csv

class Command(BaseCommand):
    """
    Custom Management Command to Import Books (& Unadded Authors)
    into the database via a csv file
    """
    help = 'Import Books (& Authors) into TGB Library via a csv file'

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
                        self.stdout.write(self.style.WARNING(f"{book.name} already exists, skipping."))
                        pass
                    except Book.DoesNotExist:
                        try:
                            country = Country.objects.get(iso3=country_iso3)
                            try:
                                author = Author.objects.get(name=author_name)
                                new_book = Book.objects.create(
                                    name=book_name,
                                    author=author,
                                    date_of_publishing=date_of_publishing,
                                    number_of_pages=number_of_pages,
                                    average_critics_rating=average_critics_rating
                                )
                                self.stdout.write(self.style.SUCCESS(f"Imported {new_book.name} authored by {author.name}"))
                            except Author.DoesNotExist:
                                self.stdout.write(self.style.WARNING(f"{author_name}: Author Does Not Exist, Creating Author"))
                                new_author = Author.objects.create(
                                    name=author_name,
                                    age=author_age,
                                    gender=author_gender,
                                    country=country
                                )
                                self.stdout.write(self.style.SUCCESS(f"Created New Author: {new_author}"))

                                new_book = Book.objects.create(
                                    name=book_name,
                                    author=author,
                                    date_of_publishing=date_of_publishing,
                                    number_of_pages=number_of_pages,
                                    average_critics_rating=average_critics_rating
                                )
                                self.stdout.write(self.style.SUCCESS(f"Imported {new_book.name} authored by {new_author.name}"))

                        except Country.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f"Break at {book_name}, Country Does Not Exist. Check if the iso3 code is valid and re-run the script."))
                            break
                self.stdout.write(self.style.SUCCESS(f"Import Complete"))