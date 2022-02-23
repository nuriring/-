Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b = 3.2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a,b = 3.2
TypeError: cannot unpack non-iterable float object
a,b=3,2
print(a=b)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a=b)
TypeError: 'a' is an invalid keyword argument for print()
a,b=3,2
print(a==b)
False
print(a!=b)
True
print(a>b)
True
priint(a<b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    priint(a<b)
NameError: name 'priint' is not defined. Did you mean: 'print'?
print(a<b)
False
print(a>=b)
True
print(a<=)
SyntaxError: invalid syntax
a=10
8<a<10
False
8<a<=10
True
a=10
a>7 and a<12
True
True#관계 연산은 논리 연산에 우선함
True
(a>7) and (a<12)
True
7<a<12
True
gender, age = "male", 20
gender == "femaile" and age >=18
False
gender == "female" or age >=18
True
gender == "femaile" or age < 18
False
a=3
not ( a>7 and a<12)
True
# ()를 사용하여 연산자의 우선순위를 강제로 명시
a,b=2,3 #0010, 0011
print(a&b) #0010 & 0011 => 0010
2
print(a|)
SyntaxError: invalid syntax
print(a|b)
3
print(a^b)
1
print(~a)
-3
print(~a) #1의 보수
-3
a=8
a=8 #0000 1000
print(a>>1) # 0000 0100
4
print(a>>2)
2
#반으로 줄어듦
print(a>>3)
1
print(a<<1) #0001 0000
16
print(a<<2)
32
print(a<<3)
64
#두배가 돼 두배가돼
#두배가 돼 두배가돼























































