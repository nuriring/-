def quicksort(arr):
    if len(arr) < 2: #두개이상일때부터 정렬가능
        return arr
    else:
        pivot = arr[-1] #피봇은 제일 마지막 값
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)

        return quicksort(smaller) + equal + quicksort(larger)


test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    unsorted_list = list(map(int, input().split()))
    print(f'#{tc} {quicksort(unsorted_list)[n//2]}')