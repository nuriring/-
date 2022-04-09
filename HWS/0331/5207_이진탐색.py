import sys
sys.stdin = open('5207.txt')
def binarySearch(n, lst, key):
    global sol
    start = 0
    end = n - 1

    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == key:
            return 1
        elif lst[middle] > key:
            end = middle - 1
            sol.append('l')
        else:
            start = middle + 1
            sol.append('r')

    return 0  # 못찾으면


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 A숫자의갯수 M은 B숫자의개수
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for number in B:
        sol = []
        result = binarySearch(N, A, number)
        print(sol,result)
        if result and len(sol) == 0:  # 바로찾는경우
            cnt += 1
            continue #continue를 해주는 이유는 이미 찾았다면 밑에 경우는 검색해보지 않도록

        if result and len(sol) == 1:  # 2. 오른쪽 한번 가고 바로 찾는 경우, 왼쪽 한번 가고 바로 찾는 경우
            cnt += 1
            continue

        flag = 1 #연속으로 좌좌 , 우우가 나왔다는 사실을 알려줄 플래그 변수 선언
        if result and len(sol) >= 2:  # 3. 오왼오왼 번갈아가면서 보다가 찾는 경우
            for i in range(len(sol) - 1): #sol 리스트를 순회하면서
                if sol[i] == sol[i + 1]: #연속으로 방향이 같은 경우를 찾는다
                    flag = 0
                    break

            if flag: #반복이 끝나도 연속으로 겹치는 경우가 없다면
                cnt += 1
            else:
                continue


    print(f'#{tc} {cnt}')

