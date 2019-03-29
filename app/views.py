from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import TemplateView

def Index(request):
    context = {
    'num_books' : models.Book.objects.all().count(),
    'num_authors': models.Author.objects.all().count(),
    'num_instances_available': models.BookInstance.objects.all().count(),
    'num_instances': models.BookInstance.objects.filter(status__exact='a').count()
    }
  
    return render(request,'app/index.html' , context)        


def Book_list(request):
    context = {
    'book_list' : models.Book.objects.all()
    }
  
    return render(request,'app/Book_list.html' , context)        

def Book_detail(request , pk):
    context = {
    'book' : models.Book.objects.filter(pk=pk)[0]
    }
  
    return render(request,'app/book_detail.html' , context)        


def Author(request):
    context = {
    'author_list' : models.Author.objects.all(),
    'test' : 'sssssss',
    }
  
    return render(request,'app/author.html' , context)        

def Author_detail(request,pk):
    return HttpResponse(pk + "DEtailsssssss")


# class Index(TemplateView):
#     template_name = "app/book.html"

#     def get_context_data(self, **kwargs):
#         context = super(Index, self).get_context_data(**kwargs)
#         context['num_books'] = '122222'
#         context['num_authors']: '22'
#         context['num_instances_available']: '3333'
#         context['num_instances']: '444'

#         return context

    # def get_context_data(self, **kwargs):
    #     context = super(Index, self).get_context_data(**kwargs)
    #     context['num_books'] : models.Book.objects.all().count()
    #     context['num_authors']: models.Author.objects.all().count()
    #     context['num_instances_available']: models.BookInstance.objects.all().count()
    #     context['num_instances']: models.BookInstance.objects.filter(status__exact='a').count()
    #     return context

