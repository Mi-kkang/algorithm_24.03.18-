def chess(i, N, li):
    global cnt

    di = [-1,-1,-1]
    dj = [-1,0,1]

    for qi, qj in li :
        for k in range(3) :
            ni = qi + di[k]
            nj = qj + dj[k]

            while 0<=ni<N and 0<=nj<N :
                if arr[ni][nj] == 1 :
                    return
                ni = ni + di[k]
                nj = nj + dj[k]

    if i == N :
        cnt += 1
        return

    for l in range(N) :
        arr[i][l] = 1
        chess(i+1, N, li + [(i,l)])
        arr[i][l] = 0




t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # NxN 보드에 N개의 퀸을 결정할 N
    arr = [[0] * N for _ in range(N)]
    cnt = 0     # 퀸을 놓는 방법의 수를 넣을 변수
    q_li = []

    chess(0,N,q_li)

    print(f'#{tc} {cnt}')