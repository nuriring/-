import sys
sys.stdin = open('5207.txt')
def binarySearch(s, e, key, direction):
    global cnt
    # 중간값 애초에 좌좌 / 우우 들은 걸러지도록 해서 제일 상단에 중간값이 키면을 넣어줘야함
    middle = (s + e) // 2
    if key == a[middle]:
        cnt += 1
        return

    elif a[middle] > key:
        if direction=='left':
            return

        binarySearch(s,middle-1,key,'left')
    else:
        if direction=='right':
            return

        binarySearch(middle+1,e,key,'right')



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 A숫자의갯수 M은 B숫자의개수
    A = list(map(int, input().split()))
    a = sorted(A)
    B = list(map(int, input().split()))
    cnt = 0
    start = 0
    end = N - 1
    direction = 'direction'
    for number in B:
        binarySearch(start, end, number,direction)
    print(cnt)




# def binarySearch(n, lst, key):
#     global cnt
#     start = 0
#     end = n - 1
#     flag = 0
#     while start <= end:
#         middle = (start + end) // 2
#         if lst[middle] == key:
#             cnt+=1
#             return
#         elif lst[middle] > key:
#             if flag==2:
#                 return
#             end = middle - 1
#             flag = 2
#         else:
#             if flag==1:
#                 return
#             start = middle + 1
#             flag = 1
#
#     return 0  # 못찾으면
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())  # N은 A숫자의갯수 M은 B숫자의개수
#     A = list(map(int, input().split()))
#     A.sort()
#     B = list(map(int, input().split()))
#     cnt = 0
#     for number in B:
#         binarySearch(N, A, number)
#
#
#     print(f'#{tc} {cnt}')
