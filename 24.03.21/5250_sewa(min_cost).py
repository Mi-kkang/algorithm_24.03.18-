from heapq import heappush, heappop

def dijkstra(si, sj) :
    pq = []     # 우선순위 큐 생성

    heappush(pq, (0,si,sj))     # 초기 가격(0원)과 위치 인큐
    cost[si][sj] = 0

    while pq :
        now, i,j = heappop(pq)  # 가격과 i좌표 j좌표 디큐

        if (i,j) == end :       # 도착이라면 리턴해주기
            return

        if cost[i][j] < now :   # 소비 가격이 더 크다면, 무시
            continue

        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]] :  # 주변을 다 돌아본다.
            ni = i + di
            nj = j + dj

            if 0<=ni<N and 0<=nj<N :
                if arr[i][j] < arr[ni][nj] :    # 다음에 가려는 곳이 경사가 더 높다면,
                    next_cost = 1 + arr[ni][nj] - arr[i][j]     # 경사를 빼주고 +1

                else :              # 경사가 같다면
                    next_cost = 1   # 1만 소비

                # 누적 가격
                new_cost = now + next_cost

                if cost[ni][nj] <= new_cost :    # 가격이 더 크거나 같으면,
                    continue                     # 넘어가기

                cost[ni][nj] = new_cost     # 낮은 가격으로 재할당
                heappush(pq, (new_cost,ni,nj))  # 다시 인큐해주기


t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # 가로, 세로의 길이 N
    arr = [list(map(int,input().split())) for _ in range(N)]    # 높이를 받는다.
    start = (0,0)       # 시작점 고정
    end = (N-1,N-1)     # 도착점 고정
    ma_v = N * N * 1000 # 높은 수 지정

    cost = [[ma_v] * N for _ in range(N)]

    dijkstra(start[0],start[1])

    ans = cost[end[0]][end[1]]

    print(f'#{tc} {ans}')