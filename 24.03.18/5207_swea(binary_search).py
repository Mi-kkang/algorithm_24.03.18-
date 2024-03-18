def binary_search(target, N) :      # 타겟 / 길이
    dir = 0         # 왔다갔다 하는지 확인하기 위한 지표 (왼쪽이면 -1 / 오른쪽이면 1)
    left = 0
    right = N - 1

    while left <= right :
        mid = (left + right) // 2

        if A[mid] == target :
            return 1
        elif A[mid] > target :  # 타겟이 가운데 정렬 했을 때 왼쪽에 있을 때,
            if dir == -1 :
                return 0
            else :
                right = mid - 1
                dir = -1
        elif A[mid] < target :  # 타겟이 가운데 정렬 했을 때 오른쪽에 있을 때,
            if dir == 1 :
                return 0
            else :
                left = mid + 1
                dir = 1

    return 0




t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # A에 속한 N개의 정수 / B에 속한 M 개의 정수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0     # 조건을 만족하는 정수의 개수를 담을 변수

    for i in range(M) :
        val = binary_search(B[i], N)
        # print(val)
        cnt += val

    print(f'#{tc} {cnt}')