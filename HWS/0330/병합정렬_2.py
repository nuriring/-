def merge_sort(numbers):
    if len(numbers) == 1:  # 길이가 1이면 그대로 리턴
        return numbers
    else:  # 길이가 2 이상일때
        mid = len(numbers) // 2  # 중간 찾기
        list1 = merge_sort(numbers[:mid])  # 왼쪽 리스트
        list2 = merge_sort(numbers[mid:])  # 오른쪽 리스트

        return merge(list1, list2)  # 두개 병합 하기


def merge(list1, list2):
    global cnt
    result = []  # 병합해서 저장할 리스트
    len_list1 = len(list1)  # 길이 저장
    len_list2 = len(list2)
    i, j = 0, 0  # i: 리스트1의 인덱스, j: 리스트2의 인덱스

    if list1[-1] > list2[-1]:  # 왼쪽 리스트의 마지막 값이 오른쪽 리스트 마지막 값보다 크면
        cnt += 1  # 변수 값 증가

    while i < len_list1 and j < len_list2:  # 하나가 끝날때 까지 비교하여 병합
        if list1[i] <= list2[j]:  # 만약 왼쪽 리스트의 현재 확인하는 값이 더 작다면
            result.append(list1[i])  # 해당 값 result에 추가하고
            i += 1  # 인덱스 증가하여 다음 숫자 탐색
        else:  # 아니라면 오른쪽 리스트에서
            result.append(list2[j])  # 해당 값 result에 추가하고
            j += 1  # 인덱스 증가

    # 반복이 끝났을 때 -> 하나의 리스트 원소가 전부 추가 되었다.
    if i < len_list1:  # 리스트1에 원소가 남아있다면
        result += list1[i:]  # 나머지 원소들 결과에 그대로 추가
    else:  # 리스트2에 원소가 남아있다면
        result += list2[j:]  # 나미저 원소들 결과에 그대로 추가

    return result  # 정렬된 리스트 반환


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    sorted_list = merge_sort(arr)

    print(f'#{tc} {sorted_list[N // 2]} {cnt}')