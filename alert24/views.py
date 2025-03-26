from django.shortcuts import render
from main.models import Categories, News

from .forms import Students

def studentView(request):
    sf = Students()
    return render(request, 'form.html', {'fm': sf})



def home(request):
    category = Categories.objects.all()
    allNews = News.objects.all().order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
                'categories':category, 
                 'allNews': allNews,
                 'topNews': topNews
              }
    return render(request, 'index.html', context)

def india(request):
    category = Categories.objects.all()
    indiaNews = News.objects.filter(category__title='India News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
                'categories':category, 
                 'indiaNews': indiaNews,
                 'topNews': topNews
              }
    return render(request, 'categories/india.html', context) 


def bolly(request):
    category = Categories.objects.all()
    bollyNews = News.objects.filter(category__title='Bollywood News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
                'categories':category, 
                 'bollyNews': bollyNews,
                 'topNews': topNews
              } 
    return render(request, 'categories/bollywood.html', context) 


def sports(request):
    category = Categories.objects.all()
    sportsNews = News.objects.filter(category__title='Sports News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
                'categories':category, 
                 'sportsNews': sportsNews,
                 'topNews': topNews
              } 
    return render(request, 'categories/sports.html', context) 


def health(request):
    category = Categories.objects.all()
    healthNews = News.objects.filter(category__title='Health News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
                'categories':category, 
                 'healthNews': healthNews,
                 'topNews': topNews
              } 
    return render(request, 'categories/health.html', context)     


def details(request, id):
     category = Categories.objects.all()
     news = News.objects.get(pk = id)
     topNews = News.objects.all().order_by('-id')[:5]
     context = {
                
                 'news': news,
                 'topNews': topNews
               } 
     return render(request, 'details.html', context)       

