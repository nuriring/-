import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    #N은 노드개수 , M은 리프노드 개수, L은 값을 출력할 노드 번호(1부터시작)
    N,M,L = map(int,input().split())
    #[ch1,ch2,parent]
    tree = [[0,0,0] for _ in range(N+1)]
    for _ in range(M):
        leafnum, num = map(int,input().split())
        #리프노드 값 입력 #자식이 없는 노드
        #부모노드 leafnum//2
        tree[leafnum] = [0,0,num]

    print(tree)
        #뒤에서부터 말단 노드에서 부터 더해나가기
    for i in range(N,1,-2): #i가 1보다 클때까지 반복
        if N%2: #정점의 개수가 홀수 일때
            tree[i//2][2] = tree[i][2] + tree[i-1][2] #부모노드의 값은 좌리프 우리프노드의 합
        else: #정점의 개수가 짝수 일때
            if i == N:
                tree[i//2][2] = tree[i][2] #하나의 리프노드만 있을경우 그대로 부모노드가 됨
            else:
                tree[i//2][2] = tree[i][2] + tree[i+1][2]
    # print(tree)
    print(f'#{tc} {tree[L][2]}')

