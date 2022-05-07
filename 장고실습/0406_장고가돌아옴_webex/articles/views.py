from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):

    '''
    모든 게시글 정보 조회
    ORM
    Model.manager.query API 
    '''
    articles = Article.objects.all()
    context = {
        'articles' : articles
    } 
    return render(request, 'articles/index.html', context)


def new(request):
    form = ArticleForm()
    print(form)
    context = {

        'form' : form
    }

    return render(request, 'articles/new.html',context)
