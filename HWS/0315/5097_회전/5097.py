import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #N은 숫자의 개수, M은 맨앞 숫자를 맨뒤로 보내는 작업의 횟수
    q = list(map(int,input().split()))
    i = 1
    while i<=M:
        check = q.pop(0)
        q.append(check)
        i+=1
    print(f'#{tc} {q[0]}')