def f(i,N,c,e) :    # i 정류장, N 종점, c 교체횟수, e 남은 배터리
    global min_v
    if e < 0 :
        return
    elif i == N :     # 종점이면
        if min_v > c :
            min_v = c
    elif min_v <= c :
        return
    else:
        f(i+1, N, c+1, arr[i]-1)    # 교체
        f(i+1, N, c, e-1)           # 통과과

t = int(input())

for tc in range(1, t+1) :
    arr = list(map(int, input().split()))       # arr[0] 종점 번호
    min_v = arr[0]

    f(2, arr[0], 0, arr[1]-1)
    print(f'#{tc} {min_v}')