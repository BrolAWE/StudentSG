from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from core.forms import RegistrationForm
from core.models import Post

from django.http import Http404


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


def news_item(request, pk):
    try:
        post_item = Post.objects.get(code=pk)
    except Post.DoesNotExist:
        raise Http404()
    return render(request, 'main/news_item.html', context={
        'post_item': post_item
    })


def contacts(request):
    return render(request, 'main/contacts.html')


def questions(request):
    return render(request, 'main/questions.html')


def registration(request):
    form = RegistrationForm()
    return render(request, 'main/registration.html', context={
        'form': form,
    })
