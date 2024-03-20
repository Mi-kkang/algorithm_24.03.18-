from collections import deque


def calcu(start, end) :
    visited = [0] * 1000001
    q = deque()
    q.append(start)
    visited[start] = 1

    while q :
        num = q.popleft()
        if num == end :
            return visited[num] - 1

        if num+1<=1000000 and visited[num+1] == 0 :
            q.append(num+1)
            visited[num+1] = visited[num] + 1

        if num-1>0 and visited[num-1] == 0 :
            q.append(num-1)
            visited[num-1] = visited[num] + 1

        if num*2<=1000000 and visited[num*2] == 0 :
            q.append(num*2)
            visited[num*2] = visited[num] + 1

        if num-10>0 and visited[num-10] == 0 :
            q.append(num-10)
            visited[num-10] = visited[num] + 1


    return -1




t = int(input())  # 테스트 케이스 개수 받기

for tc in range(1, t + 1):
    N, M = map(int, input().split())  # 시작 자연수 N / 목표 자연수 M

    ans = calcu(N,M)

    print(f'#{tc} {ans}')


