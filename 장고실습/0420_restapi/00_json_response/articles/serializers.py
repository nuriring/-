from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer): #게시글에 대한 쿼리셋을 시리얼라이저해주는 도구로서 장고가 모델폼이랑 유사하게 문법을 짜놓은 것임

    class Meta:
        model = Article
        fields = '__all__'
