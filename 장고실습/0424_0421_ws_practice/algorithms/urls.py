from django.urls import path
from . import views
urlpatterns = [
    path('problems/', views.problem_list),
    path('problems/<int:problem_pk>/', views.problem_detail),
    path('solutions/', views.solution_list),
    path('problems/<int:problem_pk>/solutions/', views.solution_create),
    path('problem/create/', views.problem_create)
]
