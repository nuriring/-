import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split()) #E는 간선의 개수 N은 시작루트
    V = E+1 #정점의 개수
    lst = list(map(int,input().split())) #간선정보
    # print(lst)
    ch1 = [0]*(V+1) #왼쪽 자식
    ch2 = [0]*(V+1) #오른쪽 자식
    for i in range(E): #간선수 만큼 반복
        parent,child = lst[i*2],lst[i*2+1]
        if ch1[parent] == 0: #왼쪽자식부터 조사해서 비어있으면
            ch1[parent] = child
        else:
            ch2[parent] = child
    print(ch1)
    print(ch2)


    #중위 순회 #좌 루트 우 #중위 순회의 시작점을 N으로 한다

    def in_order(node):
        if node:
            in_order(ch1[node])
            subtree.append(node) #바로 세어주는건 어떻게 하는걸까.. 일단모르겠으니 담아준다
            in_order(ch2[node])
        return subtree

    subtree = []
    result = len(in_order(N))
    print(f'#{tc} {result}')


