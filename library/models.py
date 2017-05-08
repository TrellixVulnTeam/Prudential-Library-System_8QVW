from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    # published_date = models.DateTimeField(blank=True, null=True, default=False)
    published_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200)
    page = models.IntegerField()

    request_user = models.CharField(max_length=5, null=True)
    # request_date = models.DateField(blank=False, null=False)
    request_date = models.DateField(auto_now_add=True)

    owner_user = models.CharField(max_length=5, null=True)

    def rental(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.title


class RentHistory(models.Model):
    isbn = models.CharField(max_length=13)
    # rental_date = models.DateField(blank=False, null=False)
    # release_date = models.DateField(blank=False, null=False)
    rental_date = models.DateField(null=False)
    release_date = models.DateField(null=True)

    rental_user = models.CharField(max_length=5, null=False)

    # def rental(self, isbn):
    #     self.isbn = isbn
    #     self.rental_date = date.today()
    #     self.rental_user = User.username

    def __str__(self):
        return self.isbn