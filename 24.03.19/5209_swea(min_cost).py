def find_cost(i, cost) :
    global min_v
    if i == N :
        if min_v > cost :
            min_v = cost

    elif cost > min_v :
        return

    for k in range(N) :
        if bit[k] != 0 :
            continue
        bit[k] = 1
        find_cost(i+1, cost+arr[k][i])
        bit[k] = 0


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1,t+1) :
    N = int(input())        # 제품 개수 N
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 99 * N          # 최소비용을 담을 변수 (무게가 제일 높을 때가 각자 99이기 때문에 초기값을 99 * (물건개수)로 정함
    bit = [0] * N

    find_cost(0,0)

    print(f'#{tc} {min_v}')