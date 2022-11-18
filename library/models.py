from django.db import models

# Create your models here.
class Country(models.Model):
    iso = models.CharField(max_length=2, null=False)
    iso3 = models.CharField(max_length=3, null=False)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Author(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    date_of_publishing = models.DateField()
    number_of_pages = models.IntegerField()
    average_critics_rating = models.IntegerField()

    def __str__(self):
        return self.name

