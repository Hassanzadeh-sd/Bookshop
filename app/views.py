from django.shortcuts import render
from django.http import HttpResponse
from . import models

def listview(request):
    context = {'latest_book_list' : models.Book.objects.all(),
    'num_books' : models.Book.objects.all().count(),
    'num_authors': models.Author.objects.all().count(),
    'num_instances_available': models.BookInstance.objects.all().count(),
    'num_instances': models.BookInstance.objects.filter(status__exact='a').count()
    }
  
    return render(request,'app/book.html' , context)

def detail(request,pk):
    return HttpResponse("booook" + str(pk))