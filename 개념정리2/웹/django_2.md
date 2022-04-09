# Django Form

### django's foms

![image-20220406221522512](django_2.assets/image-20220406221522512.png)



### Form 선언

![image-20220406221847623](django_2.assets/image-20220406221847623.png)



### Form 사용

![image-20220406222026463](django_2.assets/image-20220406222026463.png)

- ArticleForm 클래스의 인스턴스를 선언하고, form에 할당하여 context에 변수로 form을 넘겨줌
- 일일이 input과 label 태그로 form을 만들어주지 않아도 됨



### Form rendering options

![image-20220406222331741](django_2.assets/image-20220406222331741.png)



### Django의 html input 요소 표현 방법 2가지

<img src="django_2.assets/image-20220406222422238.png" alt="image-20220406222422238" style="zoom:80%;" />





### widgets

![image-20220406222529887](django_2.assets/image-20220406222529887.png)

<img src="django_2.assets/image-20220406222546477.png" alt="image-20220406222546477" style="zoom:80%;" />



### Form field 및 widget 예시

![image-20220406222948895](django_2.assets/image-20220406222948895.png)

https://docs.djangoproject.com/en/3.1/ref/forms/widgets/





### ModelForm Class

- django Form 에서 model 필드를 재정의하는 행위 중복 방지

- model을 통해 form class를 만들 수 있는 helper

- 일반 form class와 완전히 같은 방식(객체 생성)으로 view에서 사용 가능

  

### ModelForm 선언

![image-20220406223633492](django_2.assets/image-20220406223633492.png)



### Meta class

![image-20220406223807331](django_2.assets/image-20220406223807331.png)

`참고` 메타데이터 - 사진을 찍으면 촬영시각, 렌즈, 조리개 값등이 함께 저장되듯 데이터에대한 데이터!



### create view 함수 구조 변경 - 대격변! 

`참고` 위에서 아래로 작성하는 것이 아닌, 논리구조 순서대로 작성 -> 외우지말고 데이터흐름을 읽으며 코드작성

![image-20220406224655340](django_2.assets/image-20220406224655340.png)

```python
def create(request):
    if request.method == 'POST':
        #create
        form = ArticleForm(request.POST)
        # 유효성검사
        if form.is_valid():
            article = form.save() #save의 리턴값에 article이 존재 
            return redirect('articles:detail', article.pk)
        #print(form.errors) #글자크기가 넘었다고 에러를 알려주기도함
    else:
        #new
        form = ArticleForm()
    context = {
            'form' : form, #1.유효성 통과를 못한 FORM(에러메시지)과 2. 포스트 요청이 아닌 인스턴스 							form(비어있다거나) 따라서 인덴테이션을 마지막 리턴과 같은 선상에 둬야됨
    }
    return render(request, 'articles/create.html',context)

```

- **form.errors**

  ![image-20220406225841069](django_2.assets/image-20220406225841069.png)



* **is-valid()**

  <img src="django_2.assets/image-20220406224808014.png" alt="image-20220406224808014" style="zoom: 67%;" />

  

* **save() method**

  <img src="django_2.assets/image-20220406225107435.png" alt="image-20220406225107435" style="zoom: 67%;" />

```python
#create a form instance from POST data
form = ArticleForm(request.POST)
#create
# save a new Article object from the form'sdata
new_article = form.save()
#update
#create a form to edit an existing Article, but use POST data to populate the form
article = Article.objects.get(pk=1)
form = ArticleForm(request.POST, instance=article) #인스턴스!!
form.save()
```



### update 함수 구조 변경

![image-20220406225915250](django_2.assets/image-20220406225915250.png)

```python
def update(request, pk):
    if request.method == 'POST':
        #update
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article) #인스턴스가 있어야 생성x 수정o 
        # 유효성검사
        if form.is_valid():
            article = form.save() #save함수 -> 리턴값 -> article이 존재 
            						#모델폼의 save 메소드 != article.save()
            return redirect('articles:detail', article.pk)

    else:
        #edit
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
```



### DELETE 

<img src="django_2.assets/image-20220406230352583.png" alt="image-20220406230352583" style="zoom:80%;" />



### widgets 활용

- widgets 작성 기본 구조

  <img src="django_2.assets/image-20220406230434667.png" alt="image-20220406230434667" style="zoom:80%;" />

- attrs -> attributes 속성값 
- 속성값에 class를 부여해주면, 해당 클래스에 부트스트랩 클래스 속성을 입력해서 styling 가능
- 일종의 커스터마이징

- 예시

  ```python
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          widget=forms.TextInput(
              attrs={
                  'class' : 'my-title',
                  'placeholder' : 'enter the title'
                  'maxlength' : 10,
              }
          )
      )
      content = forms.CharField(
          widget=forms.Textarea(
              attrs={
                  #form-control은 부트스트랩 클래스 #CDN이 base.html에 있어야 동작
                  'class' : 'my-content form-control', 
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
  ```

`참고` forms.py는 되도록 app폴더 내에 위치

`참고` https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/ ->장고 권장 코딩스타일

### Form vs ModelForm

![image-20220406231213379](django_2.assets/image-20220406231213379.png)

`데이터만 처리 -> 폼`  ex. 로그인 --> cleaned_data 필요

`db에 값을 저장하는 등의 영향을 미침 -> 모델폼`  ex. 회원가입 --> 모델필드 속성에 맞는 html element를 만들어 주고 이를 통해 받은 데이터를 view함수에서 유효성 검사를 할 수 있도록 함

=> 무엇이 더 좋냐가 아닌, 역할에 맞춰서 취함



`참고` cleand_data구조

<img src="django_2.assets/image-20220406231830983.png" alt="image-20220406231830983" style="zoom:50%;" />



### 수동 Form 작성

**1. Rendering fields manually**

<img src="django_2.assets/image-20220406232443602.png" alt="image-20220406232443602" style="zoom:80%;" />



**1. Looping over the form;s fields ({% for %})**

<img src="django_2.assets/image-20220406232828440.png" alt="image-20220406232828440" style="zoom:80%;" />



### 부트스트랩 사용 두가지 방법

**1. Bootstrap class with widgets**

- Bootstrap Form 의 핵심 class를 widget에 작성(위에서 form-control 사용했던 것)

- 에러메시지 with Bootstrap alert 컴포넌트

  <img src="django_2.assets/image-20220406233053344.png" alt="image-20220406233053344" style="zoom:80%;" />

**2. Django Bootstrap 5 Library**

<img src="django_2.assets/image-20220406234218719.png" alt="image-20220406234218719" style="zoom: 67%;" />

`base.html` load 태그 , cdn 입력

<img src="django_2.assets/image-20220406235137238.png" alt="image-20220406235137238" style="zoom:80%;" />



`update.html` form변수를 따로 선언하지 않아도 부트스트랩 폼 형식을 선언해주면 자동으로 폼이 형성됨

![image-20220406235207671](django_2.assets/image-20220406235207671.png)

-> 대신 개별 커스텀은 어려워짐

https://django-bootstrap-v5.readthedocs.io/en/latest/





# Handling HTTP requests

### get_object_or_404

![image-20220408170826599](django_2.assets/image-20220408170826599.png)





### django view decorators

![image-20220408171046802](django_2.assets/image-20220408171046802.png)



### Allowed HTTP methods

![image-20220408171159911](django_2.assets/image-20220408171159911.png)

<img src="django_2.assets/image-20220408171258766.png" alt="image-20220408171258766" style="zoom:80%;" />



![image-20220408172157831](django_2.assets/image-20220408172157831.png)



![image-20220408172150841](django_2.assets/image-20220408172150841.png)

-> decorator를 통과해야 POST 요청이라는 의미이기 때문에 IF문 삭제가능



# Media files (이미지 업로드)

### `media file`

![image-20220408172733274](django_2.assets/image-20220408172733274.png)

### `model field`

![image-20220408172810590](django_2.assets/image-20220408172810590.png)

![image-20220408173018485](django_2.assets/image-20220408173018485.png)



### `ImageField 작성`

![image-20220408173039846](django_2.assets/image-20220408173039846.png)



### `ImageField 또는 FileField를 사용하기 위한 단계`

![image-20220408174858060](django_2.assets/image-20220408174858060.png)

### 1. media_url & media_root 설정

<img src="django_2.assets/image-20220408174922509.png" alt="image-20220408174922509" style="zoom:80%;" />



<img src="django_2.assets/image-20220409085607229.png" alt="image-20220409085607229" style="zoom:80%;" />



### 2. url 추가

![image-20220409085755338](django_2.assets/image-20220409085755338.png)



### 3. pillow 라이브러리 설치



<img src="django_2.assets/image-20220409085941644.png" alt="image-20220409085941644" style="zoom:80%;" />



### 4. form에 enctype 속성 지정

![image-20220409091811899](django_2.assets/image-20220409091811899.png)



<img src="django_2.assets/image-20220409091830154.png" alt="image-20220409091830154" style="zoom:80%;" />



### 5. views.py 수정

![image-20220409092712914](django_2.assets/image-20220409092712914.png)



### 6. 이미지 업로드 후 db 및 파일 트리 확인

![image-20220409093552268](django_2.assets/image-20220409093552268.png)



### 7. 이미지 경로 불러오기(READ 단계)

![image-20220409094041217](django_2.assets/image-20220409094041217.png)



<img src="django_2.assets/image-20220409094052435.png" alt="image-20220409094052435" style="zoom:80%;" />

<img src="django_2.assets/image-20220409094139706.png" alt="image-20220409094139706" style="zoom:80%;" />



### 8. 이미지 수정하기(UPDATE단계)

<img src="django_2.assets/image-20220409094245752.png" alt="image-20220409094245752" style="zoom:67%;" />

![image-20220409094259433](django_2.assets/image-20220409094259433.png)

![image-20220409094312432](django_2.assets/image-20220409094312432.png)

--> instance 와 달리 키워드 인자 형태로 써주지 않아도 되는 이유는 request.FILES가 인자가 두번째 위치가 기본값이기 때문임

![image-20220409094328410](django_2.assets/image-20220409094328410.png)

--> IF문 필요



### 9. 이미지 리사이징

![image-20220409095127967](django_2.assets/image-20220409095127967.png)

![image-20220409095208351](django_2.assets/image-20220409095208351.png)

![image-20220409095451850](django_2.assets/image-20220409095451850.png)

--> 200:가로 크기 / 300:세로 크기

---



![image-20220409100206121](django_2.assets/image-20220409100206121.png)

![image-20220409100547825](django_2.assets/image-20220409100547825.png)

![image-20220409100559066](django_2.assets/image-20220409100559066.png)



-------



### `upload_to argument_참고`

![image-20220408174027425](django_2.assets/image-20220408174027425.png)

<img src="django_2.assets/image-20220408174041124.png" alt="image-20220408174041124" style="zoom:80%;" />

<img src="django_2.assets/image-20220408174149983.png" alt="image-20220408174149983" style="zoom:80%;" />

<img src="django_2.assets/image-20220408174220165.png" alt="image-20220408174220165" style="zoom: 80%;" />





### `Model field option - "blank" _참고`

![image-20220408174523764](django_2.assets/image-20220408174523764.png)



### blank vs null

![image-20220408174751020](django_2.assets/image-20220408174751020.png)

![image-20220408174802132](django_2.assets/image-20220408174802132.png)

![image-20220408174812188](django_2.assets/image-20220408174812188.png)





### `input 요소의 accept 속성__참고`

![image-20220409092102099](django_2.assets/image-20220409092102099.png)

![image-20220409092116332](django_2.assets/image-20220409092116332.png)

<img src="django_2.assets/image-20220409092131356.png" alt="image-20220409092131356" style="zoom:80%;" />
