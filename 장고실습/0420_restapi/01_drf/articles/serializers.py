from dataclasses import field
from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Article,Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = '__all__' #모델폼과 유사하게 조절가능
        fields = ('id', 'title',) #json에서 id랑 title 만 보임


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) #valid 목록에서는 빠지기때문에 404 오류를 발생시키지 않고 리턴에는 포함되게 됨 -> 읽기전용