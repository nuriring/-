import sys
sys.stdin = open('input.txt')

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    lp = rp = 0 #left position , rightposition
    result = []
    while lp < len(left) and rp < len(right): #lp와 rp가 리스트 길이보다 짧은 동안
        if left[lp] < right[rp]:
            result.append(left[lp]) #작은 값을 result에 넣고
            lp += 1 #인덱스 오른쪽으로 이동
        else:
            result.append(right[rp]) #큰 값을 result에 넣고
            rp += 1 #인덱스 오른쪽으로 이동
    while lp < len(left): #왼쪽이 남아있으면
        result.append(left[lp])
        lp += 1
    while rp < len(right): #오른쪽이 남아있으면
        result.append(right[rp])
        rp += 1
    return result

def mergeSort(lst):
    if len(lst) <= 1:
        return lst  # 데이터 한개짜리 가되어서 더이상 반으로 나눌 수 없고 그 해당 한개의 데이터 들의 정렬이 끝났으니 머지하고 다시 위 스택으로 올라가라고 알려주는 역할을 함 재귀에 꼭 필요한 조건
    m = len(lst) // 2 #반씩 쪼갤거야요
    left = mergeSort(lst[:m])  # 반씩 나눠서 정렬시킴
    right = mergeSort(lst[m:])
    result = merge(left, right)
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    sorted_list = mergeSort(lst)
    print(f'#{tc} {sorted_list[N // 2]} {cnt}')
