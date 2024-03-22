def find_time(s,N,adj,D) :       # s : 시작 / N : 마지막 노드 / adj : 참고할 인접리스트 / insu : 최소비용 테이블
    U = [0] * (N+1)     # 시간이 확정된 집(노드)의 집합(visited 느낌으로)
    U[s] = 1
    D[s] = 0

    # for e, c in adj[s] :


    for _ in range(N-1) :  # 시작지를 제외한 개수 N-1번 돌기
        min_v = INF
        w = 0   # D[w]가 최소인 정점 w / 아직 정해지지 않았으니 0으로 만들기

        for i in range(1, N+1) :
            if U[i] == 0 and min_v > D[i] :
                min_v = D[i]
                w = i

        U[w] = 1    # 비용을 확정시키자

        # print(adj[w])

        for e, c in adj[w] :       # 도착지 e / 걸린시간 c
            D[e] = min(D[e], D[w] + c)



t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M, X = map(int,input().split())      # N개의 집 / M 도로의 개수 / 인수의 집 X
    adjl1 = [[] for _ in range(N+1)]        # 인접리스트 저장 (인수의 집에서 각자의 집까지 시간을 저장하기 위한 리스트)
    adjl2 = [[] for _ in range(N+1)]        # 인접리스트 저장 (각자의 집에서 인수의 집까지 시간을 저장하기 위한 리스트)
    INF = int(1e9)
    from_insu = [INF] * (N+1)               # 인수의 집에서 걸리는 시간 저장용
    to_insu = [INF] * (N+1)                 # 인수의 집까지 걸리는 시간 저장용

    for _ in range(M) :
        x, y, c = map(int,input().split())  # 시작지점 x, 도착지 y, 걸린 시간 c 받기
        adjl1[x].append([y,c])
        adjl2[y].append([x,c])

    # for i in range(1, N+1) :    # 1번 집부터 N번 집까지 본인에게 가는 거리는 0으로 만들기
    #     from_insu[i][i] = 0
    #     to_insu[i][i] = 0

    for e, c in adjl1[X] :    # 인수의 집에서 인접한 이동가능한 위치에서 걸리는 시간 저장
        from_insu[e] = c

    for e, c in adjl2[X] :    # 각자의 집 중 인수의 집까지 이동가능한 집에서 걸리는 시간 저장
        to_insu[e] = c

    find_time(X,N,adjl1,from_insu)
    find_time(X,N,adjl2,to_insu)

    max_v = 0
    for i in range(1, N+1) :
        if max_v < from_insu[i] + to_insu[i] :
            max_v = from_insu[i] + to_insu[i]

    print(f'#{tc} {max_v}')