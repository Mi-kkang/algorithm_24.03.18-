def dfs(i, N) :     # i 행에 퀸을 놓는 함수
    global cnt
    if i == N :
        cnt += 1
        return      # 모든 행에 퀸을 놓은 경우
    else :
        # i행 j열에 퀸을 놓을 수 있는 조건
        # j열에 다른 퀸이 없어야 함, 왼쪽 위, 오른쪽 위 대각선 상에도 없어야 함
        for j in range(N) :
            if col[j] == 0 and dia1[i+j] == 0 and dia2[N-1+i-j] == 0 :
                col[j] = 1
                dia1[i+j] = 1
                dia2[N-1+i-j] = 1

                dfs(i+1, N)   # 다음 행으로 이동
                col[j] = 0
                dia1[i+j] = 0
                dia2[N-1+i-j] = 0


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # NxN 보드에 N개의 퀸
    arr = [[0]*N for _ in range(N)]     # 보드판(체스판) 만들기
    cnt = 0         # 퀸을 놓는 방법의 수를 넣을 변수
    col = [0] * N
    dia1 = [0] * (N+N-1)
    dia2 = [0] * (2 * N)

    dfs(0,N)


    print(f'#{tc} {cnt}')