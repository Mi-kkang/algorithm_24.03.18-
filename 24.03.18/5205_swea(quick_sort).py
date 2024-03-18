def quickSort(arr, start, end) :
    if start >= end :   # 시작점이 끝점과 같거나 크면(다 돌았다는 의미)
        return          # 리턴해준다.

    pivot = start       # 피봇을 맨 앞 start로 잡기
    left = start + 1    # 그 뒤부터 확인
    right = end         # 맨끝까지...

    while left <= right :
        while left <= right and arr[left] <= arr[pivot] :   # 바꿀 필요가 없을 때, (피봇보다 작을 때,)
            left += 1   # 다음거 확인
        while right > start and arr[right] >= arr[pivot] :  # 바꿀 필요가 없을 때, (피봇보다 클 때,)
            right -= 1  # 하나 작은 다음거 확인

        if left > right :   # 반복문의 마지막을 때,
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else :
            arr[left], arr[right] = arr[right], arr[left]

    quickSort(arr, start, right-1)      # 정렬 기준이었던 피봇을 제외한 부분(작은쪽) 정렬 다시하기
    quickSort(arr, right+1, end)        # 정렬 기준이었던 피봇을 제외한 부분(큰쪽) 정렬 다시하기


t = int(input())    # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # 정수의 개수 N
    arr = list(map(int, input().split()))   # N개의 정수 받기
    quickSort(arr, 0, N-1)

    print(f'#{tc} {arr[N//2]}')