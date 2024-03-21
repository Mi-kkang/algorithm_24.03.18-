from heapq import heappush, heappop

def dijkstra(start) :
    pq = []     # 우선순위 큐 생성

    heappush(pq, (0,start))     # 인큐
    # 시작 노드 초기화
    distance[start] = 0

    while pq :
        # 최단거리, 노드에 대한 정보
        dist, now = heappop(pq)

        for to in graph[now] :
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            if new_dist > distance[next_node] :
                continue

            # 누적거리를 최단거리로 갱신
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))



t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, E = map(int,input().split())     # 마지막 연결지점 번호 N / 도로의 개수 E
    start = 0       # 시작지점 = 0번 지점
    val = 1000000 * 10 * 10     # 초기값으로 넣을 값 (엄청 큰 값으로)
    distance = [val] * (N+1)        # 누적 거리(가중치)를 넣을 리스트
    graph = [[] for _ in range(N+1)]  # 인접리스트로 저장 할 예정

    for _ in range(E) :
        s, e, w = map(int,input().split())  # 구간 시작 s / 구간의 끝 e / 구간 거리 w
        graph[s].append([w,e])

    dijkstra(0)
    ans = distance[N]

    print(f'#{tc} {ans}')
