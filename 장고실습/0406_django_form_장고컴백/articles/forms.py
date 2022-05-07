from distutils.log import error
from tkinter import Widget
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'enter the title',
                'maxlength' : 10,
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content form-control', #form-control 부트스트랩 스타일 지정 클래스
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={
            'required' : 'Please enter your content!!!',
        }
    )

    class Meta: 
        model = Article
        fields = '__all__' #사용자로부터 받는 모든 모델필드를 출력하게됨(지금은title,content)
        #exclude = ('title',) #제외하고 싶을 때는 한개를 제외하는게 더 효율적임

# class ArticleForm(forms.Form):
#    REGION_A = 'sl'
#    REGION_B = 'dj'
#    REGION_C = 'gj'
#    REGIONS_CHOCIES = [
#        (REGION_A,'서울'), #사용자가 서울을 클릭하면 SL이 넘어옴
#        (REGION_B,'대전'), 
#        (REGION_C,'광주'), 
#    ]
#    title = forms.CharField(max_length=10)
#    content = forms.CharField(widget=forms.Textarea)
#    region = forms.ChoiceField(choices=REGIONS_CHOCIES, widget=forms.CheckboxSelectMultiple)
#    region = forms.ChoiceField(choices=REGIONS_CHOCIES) #얘도 가능 디폴트가 설렉트