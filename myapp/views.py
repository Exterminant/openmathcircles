from django.shortcuts import render, get_object_or_404
from .models import User, Article
# Create your views here.


def home(request):
    return render(request, 'home.html')


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def articles(request):
    articles = Article.objects.all().order_by("-date_of_event")
    return render(request, 'articles.html', {'articles': articles})


def articles_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    users_events = Article.objects.filter(user_id=pk).order_by('-date_of_event')
    context = {
        'user': user,
        'users_events': users_events,
    }

    return render(request, 'user_details.html', context)

    return render(request, 'user_details.html', {})
