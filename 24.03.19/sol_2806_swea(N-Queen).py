def dfs(i, N) :     # i 행에 퀸을 놓는 함수
    global cnt
    if i == N :
        cnt += 1
        return      # 모든 행에 퀸을 놓은 경우
    else :
        # i행 j열에 퀸을 놓을 수 있는 조건
        # j열에 다른 퀸이 없어야 함, 왼쪽 위, 오른쪽 위 대각선 상에도 없어야 함
        for j in range(N) :
            if check(i,j,N) :       # 놓을 수 있으면
                arr[i][j] = 1
                dfs(i+1,N)          # 다음 행으로 이동
                arr[i][j] = 0       # i행에서 이전에 놨던 퀸 삭제


def check(i, j, N) :
    di = [-1, -1, -1]   # 다른 퀸이 있는지 검사하는 방향
    dj = [-1, 0, 1]

    for k in range(3) : # 각 방향에 대해
        ni, nj = i+di[k], j+dj[k]
        while 0<=ni<N and 0<=nj<N :
            if arr[ni][nj] == 1 :       # 퀸이 있으면
                return False            # 놓을 수 없는 자리
            ni += di[k]
            nj += dj[k]

    return True

t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # NxN 보드에 N개의 퀸
    arr = [[0]*N for _ in range(N)]     # 보드판(체스판) 만들기
    cnt = 0         # 퀸을 놓는 방법의 수를 넣을 변수

    dfs(0,N)


    print(f'#{tc} {cnt}')