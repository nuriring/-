#for 변수 in 순회할 객체:
'''
dan = int(input("단을입력하세요:")) #산술 변산을 위해 정수 변환
for i in (1,2,3,4,5,6,7,8,9): #튜플 객체의 항목을 변수에 대입
    print("{0}x{1}={2:>2}".format(dan,i,dan*i)) #:>2 두자리 폭에서 우측정렬

dan = int(input("단을입력하세요:")) #산술 변산을 위해 정수 변환
for i in range(1,10,1): #튜플 객체 대신 range(범위시작, 종료, 증감)
    print("{0}x{1}={2:>2}".format(dan,i,dan*i))

dogs = {1:"골든리트리버", 2:"진돗개", 3:"보더콜리"} #사전형 객체

for key in dogs:
    print("{0} : {1}".format(key, dogs[key]))

for key, value in dogs.items(): #<class'dict_items'>객체 사용
    print("{0} : {1}".format(key,value))
'''

'''

scores = [100, 95, 88, 98]
total = 0

for score in scores:
    total += score

print("총점:{0}".format(total))

#중첩 for문의 문법
#for 변수1 in 순회할 객체1:
    #for 변수2 in 순회할 객체2:

dan = range(2,10) #2-9
num = range(1,10) #1-9

for i in dan:
    for k in num:
        print("{0}x{1} = {2:>2}".format(i, k, i*k))
        if k==9: #true 일 경우 각 단 사이 공백
            print()
for i in dan:
    for k in num:
        print("{0}x{1} = {2:>2}".format(i, k, i*k))
    print() #바깥 for 문이 실행되기 전 무언가를 수행할 때는 안쪽 for 문 바로 밑에서 작업 처리
'''

#while 문의 문법
#while 조건식: 명령문

dan = int(input("단을 입력하세요:"))
i=1 #1부터 새로운 반복에 1씩 증가해 10까지

while i<10: #i가 10일때 false를 반환하면서 while문 종료
    print("{0}x{1}={2:>2}".format(dan,i,dan*i))
    i += 1 #i 값을 1씩 증가

scores = [100, 95, 88, 98] #리스트형
total = 0
cnt = len(scores) #cnt는 len()함수가 반환한 리스트 객체의 원소 개수 4
i = 0

while i < cnt:
    total += scores[i]
    i += 1 #변수 i의 값=4 & cnt의 값=4 일때 false를 반환하여 while문 완료

print("총점 : {0}".format(total))
'''

#break 문
answer = ""

while True:
    answer = input("명령을 입력하세요. \n'q'를 입력하면 프로그램이 종료됩니다. :")
    if answer == "q":
        break
    print("'{0}를 입력하셨습니다.".format(answer))

print("프로그램을 종료합니다...")

#continue문 : 1부터 10까지 저장되어 있는 리스트 객체에서 3의 배수를 제외한 합

numlist = [1,2,3,4,5,6,7,8,9,10]
total = 0

for n in numlist:
    if n %3 == 0:
        continue
    total += n

print("3의 배수를 제외한 총합: {0}".format(total))
'''
'''
#반복문으로 트리 만들기
# -*- coding utf-8

# for i in range(1,5):
#     print("*" * i)

# i = 1
# while i <= 4:
#     print("*" * i)
#     i = i+1
#
# for i in range(1,3):
#     for k in range(1,5):
#         print("*" * k)

# i, k = 1, 1
# while i <=2:
#     while k <=4:
#         print("*"*k)
#         k=k+1
#     i=i+1
#     k=1
#
# i, k = 5, 1
# while i >=0:
#     print("{0}{1}".format(" "*i, "*"*(2*k-1)))
#     i=i-1
#     k=k+1

# numlist = [88, 30, 61, 55, 95]
# num = 1
# for n in numlist:
#     if n >= 60:
#     	print ("{0}번 학생은 {1}점으로 합격입니다".format(num,n))
#     else:
#         print("{0}번 학생은 {1}점으로 불합격입니다".format(num,n))
#     num = num+1

a,b = 2,3
c=a+b
print("내장함수 str.format()과 print(c)를 이용한 c의 결과 출력:{0}".format(c))

'''
def 함수명 (매개변수): ->사용자 정의함수
    명령문1
    명령문2
    return문
'''
'''
#calc_sum()함수 : 두개의 값을 전달 받아 합을 구하는 사용자 정의 함수

def calc_sum(x,y): #함수 선언 위치 중요
    return x+y

a,b=2,3

c=calc_sum(a,b)
d=calc_sum(a,c)

print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과 출력:{0}".format(c))
print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과 출력:{0}".format(d))

#매개변수와 반환 값이 있는 함수
def func_parameters_return(x,y,z):
    print("매개변수로 전달된 값은 {0},{1},{2} 입니다.".format(x,y,z))
    print("매개변수와 반환값이 있는 함수입니다.")
    return "Hello, Python!"

ret_val=func_parameters_return(1,2,3)
print("func_parameters_return()함수가 반환한 값:{0}".format(ret_val)) #str.format 함수가 반환한 변환문자열을 출력

#매개변수는 없고, 반환 값이 있는 함수
def func_noparameters_return(): #no 매개변수
    print("매개변수가 없는 함수입니다.")
    return "Hello, Python!" #함수를 호출한 위치에 반환 값으로 전달

ret_val=func_noparameters_return()
print("func_noparameters_return()함수가 반환한 값:{0}".format(ret_val)) #str.format 함수가 반환한 변환문자열을 출력

#매개변수는 있고 반환 값이 없는 함수
def func_parameters_noreturn(x,y,z):
    print("매개변수로 전달된 값은 {0},{1},{2} 입니다.".format(x,y,z))
    print("반환값이 없는 함수입니다.")

func_parameters_noreturn(1,2,3)

#매개변수와 반환 값이 없는 함수
def func_noparameters_noreturn():
    print("매개변수와 반환값이 없는 함수입니다.")

func_noparameters_noreturn()

'''
'''
#매개변수 -> 함수 호출 시 입력 값을 전달 받기 위한 변수
def calc_sum(x,y,z): #함수 선언 위치 중요
    result = x+y+z
    return result

ret_val = calc_sum(1,2,3)
print("calc_sum() 함수가 반환한 값:{0}".format(ret_val))

#매개변수의 개수를 가변적으로 사용할 수 있는 언팩연산자(*) 제공, 매개변수에 적용 시 인자를 튜플 형식으로 처리

def calc_sum(*params):
    total = 0
    for val in params:
        total += val
    return  total

ret_val = calc_sum(1,2)
print("calc_sum(1,2)함수가 반환한 값: {0}".format(ret_val))

ret_val = calc_sum(1,2,3)
print("calc_sum(1,2,3)함수가 반환한 값: {0}".format(ret_val))

ret_val = calc_sum(1,2,3,4)
print("calc_sum(1,2,3,4)함수가 반환한 값: {0}".format(ret_val))

#가변형 매개변수를 가장 마지막 매개변수로 지정

#명시적 매개변수 + 가변 매개변수

def calc_sum(precision, *params): #첫번째 매개변수 precision에 인자 값이 가장 먼저 전달 -> 나머지 인자 값들이 params 매개변수에 튜플 형시으로 전달
    if precision==0:
        total =0 #매개변수 precision 값이 0이므로, 정수 0으로 초기화
    elif 0 < precision <1:
        total = 0.0

    for val in params: #매개변수 params가 1,2를 가진 튜플이므로, 두번 반복
        total += val
    return total

ret_val= calc_sum(0,1,2) #precision에 0이 params에 1,2
print("calc_sum(0,1,2)함수가 반환한 값: {0}".format(ret_val))

def calc_sum(precision, *params): #첫번째 매개변수 precision에 인자 값이 가장 먼저 전달 -> 나머지 인자 값들이 params 매개변수에 튜플 형시으로 전달
    if precision==0:
        total =0 #매개변수 precision 값이 0이므로, 정수 0으로 초기화
    elif 0 < precision <1:
        total = 0.0

    for val in params: #매개변수 params가 1,2를 가진 튜플이므로, 두번 반복
        total += val
    return total

ret_val= calc_sum(0.1,1,2) #precision에 0.1이 params에 1,2
print("calc_sum(0.1,1,2)함수가 반환한 값: {0}".format(ret_val))
'''
'''
#언팩연산자를 사용하는 튜플 형식의 반환값 : 하나의 함수로 두개의 반환값을 만들수 있음
def calc_sum(precision1, precision2, *params):
    if precision1 == 0:
        total1 = 0
    elif 0<precision1<1:
        total1 = 0.0

    if precision2 == 0:
        total2 = 0
    elif 0<precision2<1:
        total2 = 0.0
    for val in params:
        total1 += val
        total2 += val

    return total1, total2 #튜플을 반환해서 하나 이상의 값을 반환할 수 있음

ret_val = calc_sum(0, 0.1, 1, 2) #0은 precision1에 0.1은 precision2에 1,2는 params에
print("calc_sum(0,0.1,1,2) 함수가 반환한 값:{0},{1}".format(*ret_val))
print("calc_sum(0,0.1,1,2) 함수가 반환한 값:{0},{1}".format(ret_val[0],ret_val[1])) #튜플의 개별 원소를 인덱스로 접근해 처리
'''
'''
#키워드 언팩 연산자 ** : 매개변수를 딕셔너리 형식으로 처리 ex. 키1=값1

def use_keyword_arg_unpacking(**params):
    for k in params.keys(): #매개변수 params에서 함수 호출을 통해 키 리스트 구함
        print("{0}:{1}".format(k,params[k])) #key는 전달된 매개변수 이름, 값은 전달된 인자 값

print("use_keyword_arg_unpacking()의 호출")
use_keyword_arg_unpacking(a=1, b=2, c=3)
#키=값 형식으로 a=1, b=2, c=3을 전달하면, params 매개변수에 딕셔너리 형식으로 전달

#매개변수에 전달한 인자 값이 생략된 경우 사용할 기본 값 지정 *기본값을 가지는 매개변수는 일반 매개변수 앞에 위치x*

def calc(x,y,operator="+"): #"+"를 기본값으로 지정 x에 1 y에2 operator에3
    if operator=="+":
        return x+y
    else:
        return x-y

ret_val = calc(10,5,"+")
print("calc(10,5,'+')의 결과 값:{0}".format(ret_val))

ret_val = calc(10,5) #매개변수 operator의 기본값 사용
print("calc(10,5,'+')의 결과 값:{0}".format(ret_val))

ret_val = calc(10,5,"-")
print("calc(10,5,'+')의 결과 값:{0}".format(ret_val))

#scope -> 변수의 유효범위
def test_scope(a): #매개변수 a : 함수 스코프를 가지는 지역 변수
    result = a+1
    print("\n\ttest_scope() 안에서의 a의 값: {0}".format(a))
    print("\ttest_scope() 안에서의 result의 값: {0}\n".format(result))
    return result #지역변수a와 result는 유효하지 않은 정보가 됨

x=5
print("test_scope() 호출 전 x의 값: {0}".format(x))
ret_val = test_scope(x) #전역변수 x의 값 5:매개변수 a의 인자로 전달, 지역변수 result에 6저장
print("test_scope()함수가 반환한 값: {0}".format(ret_val))
print("test_scope() 호출 후 x의 값:{0}".format(x))
'''

#함수 내에서 global 변수에 접근하기
def change_global_var():
    global x #함수 내에서 x는 전역변수
    x += 1 #변수 x의 값5가 인자로 전달되고, 1을 더한 결과값 반환

x=5
change_global_var() #변수 x의 값 5가 전역변수 x의 값으로 변경
print("전역변수 x의 값:{0}".format(x))

#중첩함수
def calc(operator_fn,x,y):
    return operator_fn(x,y)
def plus(op1, op2):
    return op1 + op2
def minus(op1, op2):
    return op1 - op2

ret_val = calc(plus, 10, 5)
print("calc(plus,10,5)의 결과 값: {0}".format(ret_val))

ret_val=calc(minus, 10, 5)
print("calc(minus,10,5)의 결과 값:{0}".format(ret_val))

#람다식
def calc(operator_fn,x,y):
    return operator_fn(x,y)

ret_val = calc(lambda a,b:a+b,10,5)
print("calc(lambda a,b:a+b,10,5)의 결과 값:{0}".format(ret_val))

ret_val = calc(lambda a, b: a-b,10,5)
print("calc(lambda a,b:a-b,10,5)의 결과 값:{0}".format(ret_val))

#클로저
def outer_func():
    id = 0 #지역변수:함수 내의 코드 또는 중첩함수에서만 접근 간으

    def inner_func():
        nonlocal id #변수 id가 중첩함수인 inner_func 함수의 지역변수가 아님
        id += 1
        return id
    return inner_func #inner_func() 함수 호출x
make_id = outer_func()
print("make_id() 호출의 결과: {0}".format(make_id()))
print("make_id() 호출의 결과: {0}".format(make_id()))
print("make_id() 호출의 결과: {0}".format(make_id()))

#함수를 활용하여 원의 둘레와 면적 구하기
#-*- coding:utf-8 -*-
PI = 3.14

def input_radius():
    radius_str = input("반지름을 입력하세요:")
    return float(radius_str)

def calc_circle_area(r):
    return PI*r*r

def calc_circumference(r):
    return 2*PI*r

radius = input_radius()
circle_area = calc_circle_area(radius)
circumference = calc_circumference(radius)
print("원의 면적:{0:0.2f}, 원의 둘레:{1:0.2f}".format(circle_area,circumference))

'''

