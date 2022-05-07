from multiprocessing import managers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render,get_object_or_404, get_list_or_404 #메인페이지에 게시글이 없어도 메인페이지는 보여줘야해서 404를 쓸필요는 없지만 데이터를 보내는 경우 쿼리셋이 비어있을때 404를 보내줘야함
from .serializers import ArticleListSerializer,ArticleSerializer, CommentSerializer
from .models import Article, Comment
from articles import serializers

# Create your views here.
#@api_view() #기본값이 get
@api_view(['GET','POST']) #명시적으로 표현
def article_list(request):
    if request.method == "GET":
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST": #HTTP의 BODY 부분으로 넘어감
        serializer = ArticleSerializer(data=request.data) #첫번째자리가 instance로 자동완성이 떠서 키워드 인자로 지정해줌
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  raise_exception=True 이인자가 애초에 추가되면 이부분은 주석처리됨

@api_view(['GET','DELETE','PUT']) #명시적으로 표현
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "DELETE":
        article.delete()
        data = {
            'delete' : f'데이터 {article_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT": #put 왜 안되냐...
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET','POST']) #명시적으로 표현
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET','POST']) 
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(['GET','POST']) 
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article) #drf가 커밋을폴스보다 좀더 편의성있게 제공해주는 기능
        return Response(serializer.data, status=status.HTTP_201_CREATED)

