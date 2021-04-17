from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def news(request):
    return render(request, 'main/news.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def questions(request):
    return render(request, 'main/questions.html')


def registration(request):
    return render(request, 'main/registration.html')
