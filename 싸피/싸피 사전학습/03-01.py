Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
15
15
#리터럴의 자료형 확인 -> type 함수 활용


type(15)
<class 'int'>
type(3.14)
<class 'float'>
type('파이썬')#문자열형
<class 'str'>
type(True)
<class 'bool'>
#부울형
type([1,2,3])
<class 'list'>
#리스트형

#숫자형
#정수형, 부동소수점형, 허수형
7
7
0
0
-3
-3
342425255123
342425255123
#정수형의 길이는 무제한
0o177
127
#0o 8진수

0xdeadbeef
3735928559
#0x 16진수

0b1101
13

10.
10.0
0.001
0.001
 .001
 
SyntaxError: unexpected indent
.001
0.001
3.14ㅓ
SyntaxError: invalid decimal literal
3.14j
3.14j
#파이썬의 허수형은 j접미사

"안녕하세요"
'안녕하세요'
"5"
'5'
'홍길동'
'홍길동'
'가'
'가'
"'시간의역사'를 남긴 스티븐 호킹"
"'시간의역사'를 남긴 스티븐 호킹"
''시간의역사'를 남긴 스티븐 호킹'
SyntaxError: invalid syntax
'/'시간의역사/'를 남긴 스티븐 호킹'
SyntaxError: invalid syntax
'\'시간의역사\'를 남긴 스티븐 호킹'
"'시간의역사'를 남긴 스티븐 호킹"

"""
안녕하세요.
파이썬 프로그래밍을
시작합니다.
"""
'\n안녕하세요.\n파이썬 프로그래밍을\n시작합니다.\n'

print(\n안녕하세요.\n파이썬 프로그래밍을\n시작합니다.\n)
SyntaxError: unexpected character after line continuation character
print('\n안녕하세요.\n파이썬 프로그래밍을\n시작합니다.\n')

안녕하세요.
파이썬 프로그래밍을
시작합니다.

'''
안녕하세요.
파이썬 프로그래밍을
시작합니다.
'''
'\n안녕하세요.\n파이썬 프로그래밍을\n시작합니다.\n'
'\n안녕하세요.\n파이썬 프로그래밍을\n시작합니다.\n'
'\n안녕하세요.\n파이썬 프로그래밍을\n시작합니다.\n'

print("백슬래시\\")
백슬래시\
print("작은 따옴표 \'를 출력합니다.")
작은 따옴표 '를 출력합니다.

print("****\t****\t****\n****\t****\t****
      
SyntaxError: unterminated string literal (detected at line 1)
'SyntaxError: unterminated string literal (detected at line 1)print("****\t****\t****\n****\t****\t****
      
SyntaxError: unterminated string literal (detected at line 1)

print("****\t****\t****\n****\t****\t****")
      
****	****	****
****	****	****

"이름: %s" % "홍길동"
      
'이름: 홍길동'
"나이: %s 세" % 20
      
'나이: 20 세'
#%s는 %다음의 값을 문자열로 변환
      
"결혼: %s" % False
      
'결혼: False'
"이름: %s\n나이: %s 세" %("홍길동", 20)
      
'이름: 홍길동\n나이: 20 세'
'이름: 홍길동\n나이: 20 세'
      
'이름: 홍길동\n나이: 20 세'

"이름 : %(name)s\n나이: %(age)s 세" %{"name":"홍길동","age":20}
      
'이름 : 홍길동\n나이: 20 세'

"%c => %d" % (97, 97)
      
'a => 97'
"%d %o %x" %(10,10,10)
      
'10 12 a'
#%o는 8진수 %x는 16진수
      
"%s %d %x" %("가",ord("가"), ord("가"))
      
'가 44032 ac00'
"%f %d %(3.14, 3.14)
      
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
"%f %d" %(3.14, 3.14)
      
'3.140000 3'
"%d 점은 상위 %d%%에 속합니다." %(98,1)
      
'98 점은 상위 1%에 속합니다.'
"%10s" % "우측정렬"
      
'      우측정렬'
"%-10s" % "좌측정렬"
      
'좌측정렬      '
"%0.2f" % 3.141592
      
'3.14'
"%10.2f" % 3.121592
      
'      3.12'
"010.2f" & 3.141602
      
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    "010.2f" & 3.141602
TypeError: unsupported operand type(s) for &: 'str' and 'float'
"%010.2f" % 3.141602
      
'0000003.14'
"이름: {0}, 나이: {1} 세" .format("홍길동", 20)
      
'이름: 홍길동, 나이: 20 세'

"이름: {}, 나이: {} 세" .format("홍길동", 20)
      
'이름: 홍길동, 나이: 20 세'
'이름: 홍길동, 나이: 20 세'
      
'이름: 홍길동, 나이: 20 세'
이름: {1}, 나이: {0} 세" .format("홍길동", 20)
      
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
이름: {0}, 나이: {1} 세" .format("홍길동", 20)
      
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)이름: {1}, 나이: {0} 세" .format("홍길동", 20)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?

"이름: {1}, 나이: {0} 세" .format("홍길동", 20)
      
'이름: 20, 나이: 홍길동 세'

나이: {1}, 이름: {0} 세" .format("홍길동", 20)
      
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)나이: {1}, 이름: {0} 세" .format("홍길동", 20)
      
"나이: {1}, 이름: {0} 세" .format("홍길동", 20)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
SyntaxError: unterminated string literal (detected at line 1)나이: {1}, 이름: {0} 세" .format("홍길동", 20)

"나이: {1}, 이름: {0} 세" .format("홍길동", 20)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
SyntaxError: invalid syntax. Perhaps you forgot a comma?나이: {1}, 이름: {0} 세" .format("홍길동", 20)
      
"나이: {1}세, 이름: {0}" .format("홍길동", 20)
      
SyntaxError: unterminated string literal (detected at line 1)

"나이: {1}, 이름: {0} 세" .format("홍길동", 20)
      
'나이: 20, 이름: 홍길동 세'
"{0:c} => {1}".format(97,97)
      
'a => 97'
"{0}, {1}, {2:x}.format("가", ord("가"),ord("가"))
      
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
"{0}, {1}, {2:x}".format("가", ord("가"),ord("가"))
      
'가, 44032, ac00'

"{0:f}{1:.2f}".format(3.14,3.14)
      
'3.1400003.14'
"이름: {name}, 나이: {age} 세".format(name="홍길동", age=20)
      
'이름: 홍길동, 나이: 20 세'
"{0:<10}".format("좌측정렬")
      
'좌측정렬      '
"{0:^10}".format("중앙정렬")
      
'   중앙정렬   '
"{0:*^10}".format("중앙정렬")
      
'***중앙정렬***'
"{0:0.2f}".format(3.141592)
      
'3.14'
"{0:10.2f}".format(3.141592)
      
'      3.14'
"{0:010.2f}".format(3.141592)
      
'0000003.14'
"{{{0:.1f}}}".format(98.5)
      
'{98.5}'
