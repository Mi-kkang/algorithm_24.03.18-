def dij(s, N, adj, D) :     # s : 출발점, N : 마지막노드, adj : 참고할 인접행렬, D : 최소비용 테이블
    U = [0]*(N+1)       # U = {s}       # 비용이 결정된 노드의 집합, s 출발점
    U[s] = 1
    for _ in range(N-1) : # 출발점을 제외한 나머지 정점 만큼 반복. while U!=V << 보통은 while로 돌린다고 함... / 고정된 횟수라 for도 가능
        # V-U 원소 중에서 D[w]가 최소인 정점 w 선택
        min_w = INF     # 최소비용
        w = 0           # D[w]가 최소인 정점 w
        for i in range(1,N+1) :
            if U[i]==0 and min_w > D[i] :
                min_w = D[i]
                w = i

        U[w] = 1    # V-U 원소 중에 D[w]가 최소인 정점 w를 U에 포함
        # w에 인접한 정점에 대해, 기존 비용과 w를 거쳐가는 비용을 비교
        for i in range(1, N+1) :
            if 0 < adj[w][i] < INF :    # 0인 경우 = 자기자신 / INF인 경우 = 직접 연결된 도로가 없는 경우
                D[i] = min(D[i], D[w]+adj[w][i])


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M, X = map(int, input().split())      # N개의 집, M 도로 수, X 인수의 집

    INF = 1000000

    adj1 = [[INF]*(N+1) for _ in range(N+1)]      # 인접행렬, 인수의 집에서 귀가하는 최단 거리 구하기 용, adj[i][j]는 i에서 j로 가는 시간
    adj2 = [[INF]*(N+1) for _ in range(N+1)]

    for i in range(N+1) :   # 자기집인 경우 귀가시간 0
        adj1[i][i] = 0
        adj2[i][i] = 0

    for _ in range(M) :
        x, y, c = map(int, input().split())
        adj1[x][y] = c      # x에서 y로 가는 시간
        adj2[y][x] = c      # y에 도착하는데 걸리는 시간

    D1 = [0] * (N+1)    # X에서 각자의 집으로 귀가하는 시간 저장용
    D2 = [0] * (N+1)    #
    for i in range(1,N+1) :
        D1[i] = adj1[X][i]      # 초기 그래프에서 X에서 각 정점까지의 거리(비용)
        D2[i] = adj2[X][i]      # 각 정점에서 X에 도착하는 거리(비용/시간)

    dij(X, N, adj1, D1)
    dij(X, N, adj2, D2)
    max_v = 0
    for i in range(1, N+1) :
        if max_v < D1[i] + D2[i] :      # 왕복시간이 최대인 경우
            max_v = D1[i] + D2[i]

    print(f'#{tc} {max_v}')