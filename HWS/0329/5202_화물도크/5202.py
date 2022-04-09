import sys
sys.stdin = open('5202.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = []
    for i in range(N):
        s,e = map(int,input().split())
        lst.append((s,e))

    s_l = sorted(lst)
    s_l.sort(key=lambda x:(x[1],-x[0]))
    print(s_l)
    end = s_l[0][1]
    cnt = 1
    for i in range(len(s_l)-1):
        if end <= s_l[i+1][0]:
            cnt += 1
            end = s_l[i+1][1]
        else:
            continue
    print(f'#{tc} {cnt}')


