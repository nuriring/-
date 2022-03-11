from django.shortcuts import render, redirect, get_object_or_404
import pkg_resources
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)



def new(request):

    if request.method == 'POST' :


        title = request.POST.get('title') #QueryDict 형태로 들어있음
        content = request.POST.get('content') #QueryDict 형태로 들어있음
        
 
        article = Article()
        article.title = title
        article.content = content
        #db에 반영
        article.save()

        return redirect('articles:detail', article.pk) #

    return render(request, 'articles/new.html') 

def detail(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    #특정 게시글 조회
    # article = Article.objects.get(pk=article_pk)
    if request.method == 'POST': #조건분기!!!!
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()

    return redirect('articles:index')

def edit(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
 
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()

        return redirect('articles:detail', article.pk)
    else: #기존에 수정해야할 내용이 무엇이었는지 보여주기 위해서 들어가야함
        context = {
            'article' : article
        }
    return render(request, 'articles/edit.html',context)