from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):


def create(request):
    if request.method == 'POST':
        #create
        form = ArticleForm(request.POST)
        # 유효성검사
        if form.is_valid():
            article = form.save() #save의 리턴값에 article이 존재 #모델폼의 save 메소드는 이전에 쓰던 article.save() 이거랑은 또 다름
            return redirect('articles:detail', article.pk)
        #print(form.errors) #글자크기가 넘었다고 에러를 알려주기도함
        
        
    else:
        #new
        form = ArticleForm()
    context = {
            'form' : form, #유효성 통과를 못한 FORM(에러메시지)과 그냥 인스턴스 두가지로 나눠서 받아짐/ 인덴테이션을 마지막 리턴과 같은 선상에 둬야됨

    }
    return render(request, 'articles/create.html',context)






def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article': article,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    if request.method == 'POST':
        #update
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article) #인스턴스가 있다고 인식이 되야 수정이됨, 생성대신
        # 유효성검사
        if form.is_valid():
            article = form.save() #save의 리턴값에 article이 존재 #모델폼의 save 메소드는 이전에 쓰던 article.save() 이거랑은 또 다름
            return redirect('articles:detail', article.pk)

    else:
        #edit
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

