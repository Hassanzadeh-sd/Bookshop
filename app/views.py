from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic

class Index(generic.TemplateView):
    template_name = "app/book.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = '************'
        context['latest_book_list'] : models.Book.objects.all()
        context['num_books'] : models.Book.objects.all().count()
        context['num_authors']: models.Author.objects.all().count()
        context['num_instances_available']: models.BookInstance.objects.all().count()
        context['num_instances']: models.BookInstance.objects.filter(status__exact='a').count()
        return context


def detail(request,pk):
    return HttpResponse("booook" + str(pk))


class Booklistview(generic.ListView):
    model = models.Book

# def listview(request):
#     context = {
#     'latest_book_list' : models.Book.objects.all(),
#     'num_books' : models.Book.objects.all().count(),
#     'num_authors': models.Author.objects.all().count(),
#     'num_instances_available': models.BookInstance.objects.all().count(),
#     'num_instances': models.BookInstance.objects.filter(status__exact='a').count()
#     }
  
#     return render(request,'app/book.html' , context)
