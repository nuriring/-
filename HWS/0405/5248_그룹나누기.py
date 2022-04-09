import sys
sys.stdin = open('5248.txt')

def find_set(x):
    while x!= rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #1-N번까지 학생 #M장의 신청서
    rep = [i for i in range(N+1)]
    data = list(map(int,input().split()))
    # print(data)
    for i in range(len(data)//2):
        x,y =data[i*2],data[i*2+1]
        # if x>y:
        #     x,y = y,x
        union(x,y)
    #print(rep)
    ceo = []
    for i in rep:
        ceo.append(find_set(i))

    #print(ceo)



    print(f'#{tc} {len(set(ceo))-1}')