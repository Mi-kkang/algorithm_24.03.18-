def chess(i, N):
    global cnt
    if i == N :
        cnt += 1
        return

    else :
        for j in range(N) :
            if check(i,j,N) :
                arr[i][j] = 1
                chess(i+1, N)
                arr[i][j] = 0



def check(i, j, N) :
    di = [-1, -1, -1]
    dj = [-1, 0, 1]

    for k in range(3):
        ni = i + di[k]
        nj = j + dj[k]

        while 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 1:
                return 0
            ni = ni + di[k]
            nj = nj + dj[k]

    return 1




t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # NxN 보드에 N개의 퀸을 결정할 N
    arr = [[0] * N for _ in range(N)]
    cnt = 0     # 퀸을 놓는 방법의 수를 넣을 변수

    chess(0,N)

    print(f'#{tc} {cnt}')