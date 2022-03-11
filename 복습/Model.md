# Model

![image-20220308162414268](Model.assets/image-20220308162414268.png)

### 기본구조

![image-20220308162507824](Model.assets/image-20220308162507824.png)

![image-20220308162613217](Model.assets/image-20220308162613217.png)



### ORM(Object-Relational-Mapping)

![image-20220308162732986](Model.assets/image-20220308162732986.png)

![image-20220308163646042](Model.assets/image-20220308163646042.png)



### 사용모델필드

![image-20220308163843850](Model.assets/image-20220308163843850.png)

![image-20220308163922657](Model.assets/image-20220308163922657.png)



### Migrations

![image-20220308164026489](Model.assets/image-20220308164026489.png)

![image-20220308164259026](Model.assets/image-20220308164259026.png)

![image-20220308164315729](Model.assets/image-20220308164315729.png)

![image-20220308164532050](Model.assets/image-20220308164532050.png)

![image-20220308164957442](Model.assets/image-20220308164957442.png)

![image-20220308165527410](Model.assets/image-20220308165527410.png)



![image-20220308165710032](Model.assets/image-20220308165710032.png)

- 두 가지 비교해서 잘 알아두기



![image-20220308165933697](Model.assets/image-20220308165933697.png)



### Database API

![image-20220308170013841](Model.assets/image-20220308170013841.png)

-- **DB API 구문 - Making Queries**

![image-20220308170105264](Model.assets/image-20220308170105264.png)



![image-20220308170233689](Model.assets/image-20220308170233689.png)



### Django Shell

![image-20220308170328321](Model.assets/image-20220308170328321.png)

![image-20220308170416888](Model.assets/image-20220308170416888.png)

![image-20220308170408448](Model.assets/image-20220308170408448.png)



### CRUD

![image-20220308170514808](Model.assets/image-20220308170514808.png)



- READ 실습

  Shell_plus 실행 후

  ![image-20220308170729471](Model.assets/image-20220308170729471.png)

  전체 article 객체 조회 == DB에 인스턴스 객체를 얻기 위한 쿼리문 날리기

  이때, 레코드가 하나면 인스턴스 객체로, 두개 이상이면 쿼리셋으로 리턴



- CREATE 실습 - 1

  ![image-20220308171106443](Model.assets/image-20220308171106443.png)

  `첫번째 방법 : 인스턴스 생성 후 인스턴스 변수 설정`

![image-20220308171318680](Model.assets/image-20220308171318680.png)

- CREATE 실습 - 2

  ![image-20220308171409098](Model.assets/image-20220308171409098.png)

![image-20220308171612842](Model.assets/image-20220308171612842.png)

![image-20220308171619631](Model.assets/image-20220308171619631.png)

`두번째방법 : 초기 값과 함께 인스턴스 생성`



- CREAT 실습 - 3

  ![image-20220308171749712](Model.assets/image-20220308171749712.png)

`세번째 방법 :QuearySet API - create() 사용, 바로 쿼리 표현식을 리턴`



- CREAT 관련 메서드

![image-20220308172243874](Model.assets/image-20220308172243874.png)

![image-20220308172305492](Model.assets/image-20220308172305492.png)



### READ

![image-20220308172501177](Model.assets/image-20220308172501177.png)

![image-20220308172520129](Model.assets/image-20220308172520129.png)

![image-20220308172632082](Model.assets/image-20220308172632082.png)

![image-20220308172708762](Model.assets/image-20220308172708762.png)

![image-20220308172743218](Model.assets/image-20220308172743218.png)

![image-20220308172908195](Model.assets/image-20220308172908195.png)

![image-20220308232150037](Model.assets/image-20220308232150037.png)

https://docs.djangoproject.com/en/4.0/ref/models/querysets/#aggregate-filter  

-> 공식문서 내 queryset api methods



### Admin Site

![image-20220308232630935](Model.assets/image-20220308232630935.png)

![image-20220308232931520](Model.assets/image-20220308232931520.png)

![image-20220308233020894](Model.assets/image-20220308233020894.png)

https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options 

-> list_filter, list_display 등 다양한 modeladmin options 참고

![image-20220308233923131](Model.assets/image-20220308233923131.png)



