from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
# django는 명시적으로 경로를 표시한다
from . import views #현재폴더에서 views를 가지고옴 

# app name 역시 설정 해 줬었다.
app_name = 'articles' 

urlpatterns = [
    #path_name 이란 것을 설정 해 줘야 한다.
    path('', views.index, name='index' ),
    path('create/', views.create, name='new' ),
]
