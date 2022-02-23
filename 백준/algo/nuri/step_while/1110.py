# input 값으로 정수 받기
n = int(input())
num = n #기존 n값이 변경되면 나중에 비교할 수 없으므로 새로운 num에 할당
cnt = 0 #사이클 카운트 초기화
while True: #반복
    i = num//10 #입력값의 10의 자릿수
    j = num%10 #입력값의 1의 자릿수
    k = (i+j)%10 #각자릿수의 합의 1의 자릿수
    num = (j*10) + k #입력값의 1의 자릿수를 10의 자리로하고 k를 1의 자리로하는 새로운 수 생성
    cnt += 1 
    if num==n:
        break
print(cnt)