import sys
sys.stdin = open('5203.txt')

def babygin(lst):
    for i in range(len(lst)):  # 트리플릿 판별
        if lst[i] == 3:
            return True
    for i in range(len(lst) - 2):  # 런 판별  #10-2 , [7,8,9] #i+2를 해도 인덱스 넘어가지 않도록
        if lst[i] and lst[i + 1] and lst[i + 2]:
            return True

T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))

    p1 = [0] * 10  # 0~9까지 숫자를 인덱스를 활용해서 기록
    p2 = [0] * 10

    winner = 0
    for i in range(len(data)):  # 카드를 한장씩 나눠주면서 판별하고 있기 때문에 반복문을 돌리면서 판별
        if i % 2 == 0:
            p1[data[i]] += 1
            if babygin(p1):  # 베이비진이면
                winner = 1  # 1이 승자
                break
        else:
            p2[data[i]] += 1
            if babygin(p2):  # 베이비진이면
                winner = 2  # 2가 승자
                break

    print(f'#{tc} {winner}')
