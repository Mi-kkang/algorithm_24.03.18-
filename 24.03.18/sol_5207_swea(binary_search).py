def bsearch(t, N) :
    dir = 0         # 1 왼쪽 선택, 2 오른쪽 선택
    l = 0
    r = N-1
    result = 1      # 구간이 반복할 때의 리턴값, 반복하지 않으면 0
    while l <= r :      # 검색 구간이 존재하면,
        m = (l+r) // 2    # 중앙값
        if A[m] == t :    # key 값과 같으면
            return result       # 검색에 성공하면, result를 리턴
        elif A[m] > t :
            r = m - 1
            if dir == 1 :       # 이전에도 왼쪽을 선택한 경우
                result = 0
            dir = 1
        elif A[m] < t :
            l = m + 1
            if dir == 2 :
                result = 0
            dir = 2
    return 0





t = int(input())

for tc in range(1, t+1) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0

    for x in B :
        cnt += bsearch(x, N)

    print(f'#{tc} {cnt}')