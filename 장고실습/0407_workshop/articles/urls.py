from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'), #동일url을 사용함으로써 detail에 먼저 먹혀서 delete가 제대로 동작을 안하기 때문에 delete 를 url경로에 추가해줌
    path('<int:article_pk>/update/', views.update, name='update'), 
    
]
