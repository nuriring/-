from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article, Comment, HashTag
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            for word in article.content.split(): #본문 내용중에 #으로 시작되는 문장만 거르기
                if word.startswith('#'):
                    print(word)
                    hashtag, boolean = HashTag.objects.get_or_create(content=word) #생성했으면 true #이미 있어서 생성안했으면 false
                    article.hashtags.add(hashtag)
                    
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # 조회한 article의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                # 모든 hashtag와의 관계 제거
                article.hashtags.clear()
                for word in article.content.split(): #본문 내용중에 #으로 시작되는 문장만 거르기
                    if word.startswith('#'):
                        hashtag, boolean = HashTag.objects.get_or_create(content=word) #생성했으면 true #이미 있어서 생성안했으면 false
                        article.hashtags.add(hashtag)
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comment_delete(request, article_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)



@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article,pk=article_pk)
        # 누르는게 무조건 좋아요를 활성화만 시킬까"?
        # 게시글에 좋아요를 누른 유저 목록에 현재 요청하는 유저가 있다면 좋아요를 취소
        if request.user in article.like_users.all(): #in대신 exit() 코드 사용 방법 교재애있음
            article.like_users.remove(request.user) 
        # 좋아요 가능
        else:
            article.like_users.add(request.user)
        
        return redirect('articles:index')
    return redirect('accounts:login')


def hashtag(request, hash_pk):
    hash = get_object_or_404(HashTag, pk=hash_pk)
    # 이 해시태그와 연결된 모든 게시글들
    articles = hash.articles.all()
    context = {
        'hash' : hash,
        'articles' : articles
    }
    return render(request, 'articles/hash.html', context)