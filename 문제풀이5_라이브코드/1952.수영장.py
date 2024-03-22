import sys
sys.stdin = open("input.txt", "r")


def dfs(month, sum_cost):
    global ans

    # 기저조건
    # 1. 12월까지 다 봤네? 종료
    if month > 12:
        # 최소 비용
        ans = min(ans, sum_cost)
        return

    # 2. 이미 최소값을 넘어갔네? 종료
    if sum_cost > ans:
        return

    # 모두 1일권으로 구매
    dfs(month + 1, sum_cost + (days[month] * cost[0]))

    # 1달권 구매
    dfs(month + 1, sum_cost + cost[1])

    # 3달권 구매
    dfs(month + 3, sum_cost + cost[2])

    # 1년권 구매
    dfs(month + 12, sum_cost + cost[3])


T = int(input())

for tc in range(1, T + 1):
    cost = list(map(int, input().split()))
    # 아 인덱스 너무 머리아파!
    # 1부터 쓸래 (맨 앞에 0 쓰레기값 넣을래 )
    days = [0] + list(map(int, input().split()))
    ans = int(1e9)
    dfs(1, 0)
    print(f'#{tc} {ans}')
