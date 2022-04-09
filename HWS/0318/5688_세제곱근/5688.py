import sys
sys.stdin = open('input.txt')
# import time
# start = time.time()  # 시작 시간 저장
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     num = N
#     X = -1
#     i=1
#
#     for i in range(1,N+1):
#         if num//i == i**2:
#             num = num//i
#             if num//i == i:
#                 X = i
#                 break
#
#     print(f'#{tc} {X}')
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

##범위가 10의 18승까지니까 전부다 탐색 안하고
## 10의 6승까지만 탐색할수 있음
threeroot = list(i for i in range(1,1000001)) #세제곱근 후보 저장

T = int(input())

for tc in range(1,T+1):
    X = -1
    N = int(input())
    for i in threeroot:
        if i**3 == N:
            X = i
    print(f'#{tc} {X}')