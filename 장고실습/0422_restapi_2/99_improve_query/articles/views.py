from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count

# Create your views here.
def index_1(request):
    #articles = Article.objects.order_by('-pk')
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)


def index_2(request):
    #articles = Article.objects.order_by('-pk')
    articles = Article.objects.select_related('user').order_by('-pk') #1:N관계에서 1인 user를 한번에 같이 가져와버린다.
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)


def index_3(request):
   # articles = Article.objects.order_by('-pk') 
    #article에 달린 댓글까지 이번엔 N개를 한번에 가져오기
    articles = Article.objects.prefetch_related('comment_set')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)


from django.db.models import Prefetch


def index_4(request):
    #articles = Article.objects.order_by('-pk')
    articles = Article.objects.prefetch_related('comment_set')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
