# import sys
# sys.stdin = open('input.txt', r)

# prim 알고리즘
'''
7 11
# 노드 7개 간선 11개
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 우선순위큐를 활용
from heapq import heappush, heappop

def prim(start) :
    pq = []
    MST = [0] * V       # 최소비용신장트리 / visited와 같은 내용

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [PRIM] 우선 순위가 가중치에 따라 정렬 // 가중치가 낮으면 먼저 나와야 한다.
    #   -> 관리해야 할 데이터 : 가중치, 노드 번호 => 2가지
    #   -> 동시에 두 가지 데이터 다루기
    #       1. class로 만들기   --> 인자가 3가지 이상이면 클래스가 낫다. (2가지 까지는 튜플로)
    #       2. 튜플로 관리
    # 이차원 배열 + 가중치 + 높이
    heappush(pq, (0, start))    # 가중치와 노드 번호 튜플로 저장)

    while pq :
        weight, now = heappop(pq)

        print(now, '/', MST)

        # 우선순위 큐의 특성 상
        # 더 먼거리로 가는 방법이 pq에 저장이 되어있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면, continue
        if MST[now] :
            continue

        # 방문처리
        MST[now] = 1
        # 누적합 추가(가중치 추가)
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V) :
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] == 0 or MST[to] :
                continue

            heappush(pq, (graph[now][to], to))


    print(f'min cost : {sum_weight}')




V, E = map(int, input().split())
# 인접 행렬로 저장
# - [실습] 인접 리스트로 저장해서 해보기!
graph = [[0]*V for _ in range(V)]
for _ in range(E) :
    s, e, w = map(int, input().split())
    # 가중치 저장
    # [기존] 3 -> 4로 갈 수 있다.
    # graph[3][4] = 1

    # [가중치 그래프] 3 -> 4로 가는데 31이라는 비용이 든다.
    # graph[3][4] = 31
    graph[s][e] = w
    graph[e][s] = w     # 무방향 그래프 (서로 왔다갔다 할 수 있다)


prim(0)
