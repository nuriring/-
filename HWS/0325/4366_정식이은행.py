import sys
sys.stdin = open('4366.txt')


def solve(lst2,lst3):
    for i in range(len(lst2)):
        #1비트 값만 바꿔서 10진수 값으로 변환
        lst2[i] = (lst2[i]+1) %2
        dec = 0
        for idx in range(len(lst2)):
            dec = dec*2 + lst2[idx]
        s = []# 3진수로 변환
        ret = dec
        while dec>0:
            s.append(dec%3)
            dec //= 3
        #담는순서를 뒤집어줘야 진수표현이 되니깐
        lst = s[::-1]


        cnt = 0
        for idx in range(min(len(lst),len(lst3))): #두개의 길이중에 짧은것만큼
            if lst[idx] != lst3[idx]:
                cnt+= 1
        cnt += abs(len(lst)-len(lst3)) #길이가 다르다면 하나만 달라도 걸러줘야 하니까 다른 값을 넣어준다

        if cnt == 1:
            return ret

        lst2[i] = (lst2[i]+1)%2 #원상복구
T = int(input())
for tc in range(1,T+1):
    lst2 = list(map(int,input()))
    lst3 = list(map(int,input()))
    ans = solve(lst2,lst3)
    print(f'#{tc} {ans}')