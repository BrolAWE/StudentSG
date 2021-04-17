from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from core.models import Post


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', context={
        'page_obj': page_obj,
    })


def about(request):
    return render(request, 'main/about.html')


def news(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/news.html', context={
        'page_obj': page_obj,
    })


def contacts(request):
    return render(request, 'main/contacts.html')


def questions(request):
    return render(request, 'main/questions.html')


def registration(request):
    return render(request, 'main/registration.html')
