def find_queen(i, q_li, ch) :       # i : 행의 위치(행은 다 다르게 해줄 예정 / 우리는 열과 대각선만 확인) / q_li : 퀸의 위치를 담은 리스트
    global cnt

    for qi, qj in q_li :

        # 열을 확인할 예정
        ci = qi - 1
        cj = qj

        while 0<=ci<N and 0<=cj<N :
            if arr[ci][cj] == 1 :       # 같은 열에 퀸이 있다면,
                return                  # 리턴
            ci = ci - 1


        # 대각선을 확인할 예정
        di = qi - 1
        dj = qj + 1

        while 0<=di<N and 0<=dj<N :
            if arr[di][dj] == 1 :       # 대각선에 퀸이 있다면,
                return                  # 리턴
            di = di - 1
            dj = dj + 1

        di2 = qi - 1
        dj2 = qj - 1

        while 0 <= di2 < N and 0 <= dj2 < N:
            if arr[di2][dj2] == 1:  # 대각선에 퀸이 있다면,
                return                  # 리턴
            di2 = di2 - 1
            dj2 = dj2 - 1


    if i == N:
        cnt += 1
        return

    else :

        for k in range(N) :
            arr[i][k] = 1
            q_li.append((i,k))
            find_queen(i+1, q_li, ch)
            q_li.pop()
            arr[i][k] = 0


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # NxN 보드에 N개의 퀸
    arr = [[0]*N for _ in range(N)]     # 보드판(체스판) 만들기
    cnt = 0         # 퀸을 놓는 방법의 수를 넣을 변수
    li = []         # 퀸의 위치를 넣을 리스트
    check = True

    find_queen(0, li, check)

    print(f'#{tc} {cnt}')