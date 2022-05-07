from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Enter the title',
                'class' : 'form-control',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'Enter the content',
                'class' : 'form-control',
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'