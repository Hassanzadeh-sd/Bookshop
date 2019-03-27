from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name=       models.CharField(max_length=200 , help_text="Enter a book genre")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name=     models.CharField(max_length=100)
    last_name=      models.CharField(max_length=100)
    date_of_birth=  models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        return '%s , %s' % (self.last_name, self.first_name)

class Book(models.Model):
    title=      models.CharField(max_length=200)
    author=     models.ForeignKey(Author, on_delete=models.CASCADE , null=True)
    summary=    models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn=       models.CharField('ISBN', max_length=13, help_text="13 character <a href=")
    genre=      models.ManyToManyField(Genre,help_text="select a genre for this book")

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

class BookInstance(models.Model):
    id=         models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book")
    book=       models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint=    models.CharField(max_length=200)
    due_back=   models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status=     models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m' , help_text="Book avilable status")

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)

    def __unicode__(self):
        return 