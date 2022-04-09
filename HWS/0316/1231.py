import sys
sys.stdin = open('1231.txt')

def in_order(node):
    #해당 노드가 있으면
    if node: #우리가 0으로 초기화를 해놨으니깐 #냅다 잎노드까지 가서 확인해보자
        #해당 노드의 왼쪽 조사
        in_order(int(tree[node][2]))
        print(f'{tree[node][1]}',end="") #처리는 루트에서만 한다
        in_order(int(tree[node][3])) #오른쪽 조사

for tc in range(1,11):
    N = int(input()) #정점의 총수
    # tree = [[0,0,0,0] for _ in range(N+1)]
    # print(tree)
    tree = [[0]]
    for _ in range(N): #N줄에 걸쳐 정점 정보
        lst = list(input().split())
        tree.append(lst)
    print(tree)
    for i in tree:
        # print(i)
        if len(i)<=3:#인덱스에러방지를 위해서 0패딩
            while len(i)!=4:
                i.append('0')
    print(tree)
    print(f'#{tc}',end=" ")
    in_order(1)
    print()


