def work_work(i,val) :
    global max_v
    if i == N :
        if max_v < val :
            max_v = val
        return

    elif max_v >= val :
        return

    for k in range(N) :
        if bit[k] != 0 :
            continue

        bit[k] = 1
        work_work(i+1, (val * (arr[i][k] * (1/100))))
        bit[k] = 0


t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1,t+1) :
    N = int(input())        # 직원, 할 일 N개
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0           # 성공할 확률이 최대인 값을 저장할 변수
    bit = [0]*N         # 비트를 만들어요

    work_work(0,1)

    ans = max_v * 100

    print(f'#{tc} {ans:.6f}')