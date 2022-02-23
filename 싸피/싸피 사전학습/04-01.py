Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=10
10
10
str="홍길동"
type(lst)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(lst)
NameError: name 'lst' is not defined. Did you mean: 'list'?
type(list)
<class 'type'>
a=3.14
a="파이썬"
a=True

var1=10
var2=10
var1 is var2
True
var3 =2-
SyntaxError: invalid syntax
var3=20
var1isvar3
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    var1isvar3
NameError: name 'var1isvar3' is not defined
var1 is var3
False
x,y = 10, 20
x
10
y
20
x<y
True
x>y
False
under18=false
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    under18=false
NameError: name 'false' is not defined. Did you mean: 'False'?
under18=False
male=True
under18 and male
False
if under18:
    print("미성년자입니다.")
else:
    print("성년입니다.")

    
성년입니다.
student=("홍길동", 20)
student="홍길동", 20
student
('홍길동', 20)
student[0]
'홍길동'
student[1]
20
student[2]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    student[2]
IndexError: tuple index out of range
#유효인덱스 0~!
student[1]=21
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    student[1]=21
TypeError: 'tuple' object does not support item assignment
TypeError: 'tuple' object does not support item assignment# 튜플은 한번 저장된 값은 변형 x
SyntaxError: invalid syntax

student=("임꺽정", 30)
student
('임꺽정', 30)
student=["홍길동", 20]
student
['홍길동', 20]
student[0]
'홍길동'
student[1]
20
student[2]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    student[2]
IndexError: list index out of range
#유효인덱스 0~1
['홍길동', 21]
['홍길동', 21]
student[2]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    student[2]
IndexError: list index out of range
['홍길동', 21]
['홍길동', 21]
student=["임꺽정", 30]
studnt
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    studnt
NameError: name 'studnt' is not defined. Did you mean: 'student'?
student
['임꺽정', 30]
student={"홍길동", "이순신", "강감찬", "홍길동"}
student
{'강감찬', '홍길동', '이순신'}
student[0]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    student[0]
TypeError: 'set' object is not subscriptable
student :={"을지문덕", "이순신"}
SyntaxError: invalid syntax
student ={"을지문덕", "이순신"}
student
{'을지문덕', '이순신'}
student={"을지문덕", "이순신"}
student

student
{'을지문덕', '이순신'}

student={"임꺽정",30}
student
{'임꺽정', 30}
dogs={1:"골든리트리버", 2:"진돗개", 3:"보더콜리"}
dogs
{1: '골든리트리버', 2: '진돗개', 3: '보더콜리'}
dogs[1]
'골든리트리버'
dogs[2]
'진돗개'
dogs[3]
'보더콜리'
dogs[4]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dogs[4]
KeyError: 4
dogs[2]='레브라도리트리버'
dogs
{1: '골든리트리버', 2: '레브라도리트리버', 3: '보더콜리'}
dogs["4"]="알래스카"
dogs
{1: '골든리트리버', 2: '레브라도리트리버', 3: '보더콜리', '4': '알래스카'}
dogs[4]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    dogs[4]
KeyError: 4
dogs["4"]
'알래스카'
dogs={}
dogs
{}
obj
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    obj
NameError: name 'obj' is not defined
obj=None
obj is None
True
OBJ==None
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    OBJ==None
NameError: name 'OBJ' is not defined. Did you mean: 'obj'?
obj==None
True
if obj:
    print("obj는 None이 아닙니다.")
    else:
        
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
if obj:
    print("obj는 None이 아닙니다.")
    else: print("obj는 None입니다.")

SyntaxError: invalid syntax
if obj:
    print("obj는 None이 아닙니다.")
    else: print("obj는 None입니다.")
    
SyntaxError: invalid syntax

if obj:
    print("obj는 None이 아닙니다.")
    else:
        
SyntaxError: invalid syntax
if obj:
    print("obj는 None이 아닙니다.")
else:
    print("obj는 None입니다.")

    
obj는 None입니다.

if not obj:
    print("obj는 None입니다.")
else:
    print("obj는 None이 아닙니다.")

    
obj는 None입니다.

x=y=10
x
10
y
10
x,y =(10,20)
x,y=10,20
(x,y)=(10,20)
x
10
y
20
x,y=[10,20]
[x,y]=10,20
[x,y]=[10,20]
x
10
y
20
x,y=y,x
x
20
y
10
x=10
y=20
del(x)
del(y)
x
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    x
NameError: name 'x' is not defined
y
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    y
NameError: name 'y' is not defined
