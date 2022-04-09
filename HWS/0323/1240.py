import sys
sys.stdin = open('1240.txt')
from pprint import pprint

password = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #세로, 가로
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(M-1,-1,-1): #뒤에서 부터 조사
            if arr[i][j] == '1': #암호를 만들고 암호가 정상인지 확인까지 해야함
                pointi, pointj = i,j
                break

    result = ''
    while pointj-7>0:
        if arr[pointi][pointj-6:pointj+1] in password:
            result = str(password[arr[pointi][pointj-6:pointj+1]]) + result
            pointj -= 7
        else:
            pointj -= 1
    # 암호를 만들었으니 정상인지 확인
    # print(result)
    evensum = 0
    oddsum = 0
    for i in range(7):
        if i%2==0:
            oddsum += int(result[i])
        else:
            evensum += int(result[i])
    check = evensum+oddsum*3+int(result[7])
    if check%10 == 0:
        ssum = 0
        for j in range(8):
            ssum += int(result[j])
        print(f'#{tc} {ssum}')
    else:
        print(f'#{tc} 0')

