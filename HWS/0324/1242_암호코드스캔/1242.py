import sys
sys.stdin = open('1242.txt')
from pprint import pprint

#0~9,A~F 7 --> 0111, A --> 1010 , F --> 1111
def hextobin(hexV):
    #16진수를 10진수로
    if 'A' <= hexV <='F' :
        decV = ord(hexV) - ord('A') + 10
    else:
        decV = int(hexV)
    #10진수를 2진수로
    result = ''
    for i in range(4):
        if decV & (8>>i):
            result += '1'
        else:
            result += '0'
    return result
    # if decV & 8: 8>>0#0b1000 : 8/0
    # if decV & 4: 8>>1
    # if decV & 2: 8>>2

sCode = {211:0, 221:1, 122:2, 411:3, 132:4, 231:5, 114:6, 312:7, 213:8, 112:9}

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #세로, 가로
    arr = [input() for _ in range(N)]
    arr2 = [''for _ in range(N)]
    for i in range(N):
        for j in range(M):
            arr2[i] += hextobin(arr[i][j])
    # pprint(arr)
    # pprint(arr2)
    # 상단의 우측부터 코드의 끝지점을 찾아보자
    ssum = 0
    for y in range(1, N): #첫번째 줄에 암호가 있을수도 있으니까 y는 1부터
        # for x in range(M*4-1,-1,-1): #이렇게 찾으면 어려움
        x = M*4-1
        while x > 0:
            numbers = ['-'] * 8
            #코드의 오른쪽 끝을 찾은거임
            if arr2[y][x] == '1' and arr2[y-1][x] == '0':
                for i in range(7, -1, -1): #찾았으면 8번반복
                    cnt1 = 0
                    while arr2[y][x] == '1': #오른쪽끝에 1의 개수 세기
                        cnt1 += 1
                        x -= 1
                    #다음 0의 갯수
                    cnt2 = 0
                    while arr2[y][x] == '0':
                        cnt2 += 1
                        x -= 1
                    #다음 1의 갯수
                    cnt3 = 0
                    while arr2[y][x] == '1':
                        cnt3 += 1
                        x -= 1
                    #'0'만큼 앞으로 이동
                    while arr2[y][x] == '0':
                        x -= 1
                    #두께를 찾는다.
                    # print(cnt1,cnt2,cnt3)
                    k = min(cnt1,cnt2,cnt3)
                    numbers[i] = sCode[cnt3//k*100 + cnt2//k*10 + cnt1//k] #비율고려
                # print(numbers)
                oddnum = numbers[0] + numbers[2] + numbers[4] + numbers[6]
                evennum = numbers[1] + numbers[3] + numbers[5] + numbers[7]
                if (oddnum*3 + evennum)%10==0:
                    ssum += sum(numbers)


            else: #못찾았으면 if안으로 못들어가니까 따로 앞으로 이동하는거 넣어줘야함
                x -= 1

    print(f'#{tc} {ssum}')






