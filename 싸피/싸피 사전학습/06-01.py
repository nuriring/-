Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b=3,2
print("{0}+{1}={2}".format(a,b,a+b))
3+2=5
print("{0}-{1}={2}".format(a,b,a-b))
3-2=1
print("{0}*{1}={2}".format(a,b,a*b))
3*2=6
print("{0}/{1}={2}".format(a,b,a/b))
3/2=1.5
print("{0}//{1}={2}".format(a,b,a//b))
3//2=1
print("{0}%{1}={2}".format(a,b,a%b))
3%2=1
print("{0}**{1}={2}".format(a,b,a**b))
3**2=9
a,b,c=2,3,5
print((a+b)-c)
0
print(b-c+a)
0
print(a+(b*c))
17
print(a*b/c)
1.2
print((a+b)-c)
0
print(a+(b-c))
0
print(a+9b*c))
SyntaxError: invalid decimal literal
print((a+b)*c)
25
print(a*(b/c))
1.2
a,b,c="2","3",4
print(a+b)
23
print(int(a)+int(b)) #문자열 "2"는 정수2로
5
print(b+c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(b+c)
TypeError: can only concatenate str (not "int") to str
priint(int(b)+c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    priint(int(b)+c)
NameError: name 'priint' is not defined. Did you mean: 'print'?
print(int(b)+c)
7
print(b+str(C))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(b+str(C))
NameError: name 'C' is not defined. Did you mean: 'c'?
print(b+str(c))
34
a=10
a+=5; print(a)
15
a-=5; print(a)
10
a*=5;print(a)
50
a/=5;print(a)
10.0
#나누기 연산 부동소수점 반영
a//=5;print(a)
2.0
a%=5;print(a)
2.0
a**=5;print(a)
32.0
a,b=3,2
print(a=)
SyntaxError: invalid syntax
print(a=b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(a=b)
TypeError: 'a' is an invalid keyword argument for print()
a,b=3,2
print(a=b)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(a=b)
TypeError: 'a' is an invalid keyword argument for print()
print(a = b)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(a = b)
TypeError: 'a' is an invalid keyword argument for print()
a,b=3,2
print(a = b)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(a = b)
TypeError: 'a' is an invalid keyword argument for print()
a,b = 3,2
print(a = b)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(a = b)
TypeError: 'a' is an invalid keyword argument for print()
dle(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dle(a)
NameError: name 'dle' is not defined
