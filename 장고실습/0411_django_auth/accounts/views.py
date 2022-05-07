from ast import Pass
from django.shortcuts import render,redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST
from .forms import CustomUserChangeForm

# Create your views here.
@require_http_methods(['GET','POST'])
def login(request):
    data = request.GET.get('next') #'/articles/create/'
    if request.user.is_authenticated: #로그인이 되어있으면 로그인과 관련된 로직은 진행하면 안됨
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            #print(request.session)
            auth_login(request, form.get_user()) #auth form을 통해서 인증된 user 객체가 instance method로 전달됨
            # print(request.session)
            # print(request.session.keys())
            return redirect(request.GET.get('next') or 'articles:index')

    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated: #로그인된 사용자만 로그아웃 호출 가능
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) #회원가입하자마자 바로 로그인해주는 시스템 #필수는 아님
            return redirect('articles:index')

    else:
        form = UserCreationForm()
    context={
        'form':form
    }

    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        #주의 반드시 회원탈퇴 후 로그아웃 함수 호출
        request.user.delete()
        auth_logout(request) #유저도 테이블에서 지우고, 세션도 지워버리고 싶다면 #순서 주의 먼저 유저를 지우고 그다음에 로그아웃
    return redirect('articles:index')

@login_required
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context={
        'form':form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)
