import sys
sys.stdin = open('4880.txt')


def match(data, left, right):
    # 그룹에 남아 있는 사람이 한명이 될 때 까지
    # 왼쪽과 오른쪽의 idx 값이 같아 질 때 까지
    if left == right:
        # 왼쪽 오른쪽 상관없이 번호 출력
        return left

    # 중간값을 나누는 조건 : 문제에 나와 있음.
    middle = (left + right) // 2

    # 중간값을 기준으로 왼쪽, 오른쪽 그룹 계속 나눌거임
    left_group = match(data, left, middle)
    right_group = match(data, middle+1 ,right)

    # # 숫자 1은 가위, 2는 바위, 3은 보
    # if data[left_group] == data[right_group]:
    #     return left_group
    #
    # # 왼쪽이 가위일때
    # if data[left_group] == 1:
    #     # 오른쪽이 바위
    #     if data[right_group] == 2:
    #         return right_group
    #     else:
    #         return left_group
    #
    # # 왼쪽이 바위일때
    # if data[left_group] == 2:
    #     # 오른쪽이 가위
    #     if data[right_group] == 1:
    #         return left_group
    #     else:
    #         return right_group
    #
    # # 왼쪽이 보일때
    # if data[left_group] == 3:
    #     # 오른쪽이 가위
    #     if data[right_group] == 1:
    #         return right_group
    #     else:
    #         return left_group

    # 숫자 1은 가위, 2는 바위, 3은 보
    # (1 - 2) % 3 = 2 | 승자는 바위 (오른쪽 승) #파이썬에서는 음수를 나눈 나머지를 A%B일때 A가 음수라면 A에 B를 계속 더해서 양수가 되면 그때 B로 나눈 나머지를 출력한다
    # (3 - 2) % 3 = 1 | 승자는 보 (왼쪽 승)
    # (2 - 2) % 3 = 0 | 무승부 (무승부는 왼쪽이 이기기로 했어요)
    winner = (data[left_group] - data[right_group]) % 3
    if winner == 2 :
        return right_group
    else:
        return left_group

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    # 최종 결과를 반환 받기 위한
    # 선수목록, 맨 왼쪽 선수 번호, 가장 오른쪽 선수 번호
    result = match(data, 0, N-1) #인덱스를 기준으로 계산하기 떼문에
    print(f'#{tc} {result+1}') #결과에 +1








