# 문제조건
# 크로아티아 알파벳 갯수 세기
# 입력 문자
word = (input())
# 크로아티아 알파벳 1개로 치환되는 문자열 리스트 
list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for i in list:
    if i in word:
        word = word.replace(i,"_") #알파벳 한개가 '_' 로치환 
print(len(word)) 