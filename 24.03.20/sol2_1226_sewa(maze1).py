def find_start() :
    for i in range(16) :
        for j in range(16) :
            if maze[i][j] == 2 :
                return i, j


def dfs(i, j) :     # 중복없이 빠짐없이 1번만 방문
    stack = []      # stack 생성
    visited = [[0]*16 for _ in range(16)]
    stack.append((i,j))     # 시작점 push
    visited[i][j] = 1          # 시작점 메우기

    while stack :
        i, j = stack.pop()      # 갈림길 중 하나를 꺼내 탐색 시작
        # if maze[ni][nj] == 3 :    # visited를 사용하면 여기서도 확인 가능
        #       return 1
        # 인접한 칸을 모두 push (선택가능한 방향을 모두 push)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :
            ni, nj = i + di, j + dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj] != 1 and visited[ni][nj]==0:
                if maze[ni][nj] == 3 :
                    return 1
                stack.append((ni,nj))   # push
                visited[ni][nj] = 1        # visited[ni]nj] = 1

    return 0



t = 10

for tc in range(t) :
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]

    i, j = find_start()
    print(f'#{tc} {dfs(i,j)}')