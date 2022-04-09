import sys
sys.stdin = open('5185.txt')
T = int(input())
for tc in range(1,T+1):
    N,NUM = map(str,input().split()) #문자열로받아옴
    # print(NUM)
    bit = '' #전체를 4비트 2진수로 바꿔서 넣어줄 문자열
    #16-> 10진수로 먼저 바꾸자
    for i in range(len(NUM)):
        tmp = int(NUM[i],16)
        # print(tmp)
        #10진수 -> 2진수
        tmp = bin(tmp).replace('0b', '')
        # print(tmp)
        #4비트 2진수화
        while len(tmp) != 4:
            tmp = '0' + tmp  # 주의 뒤가 아니라 앞에붙여줘야함
        # print(tmp) #4자리 맞춰줌
        bit += tmp
    print(f'#{tc} {bit}')

