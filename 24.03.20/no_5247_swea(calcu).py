def calcu(i,goal,cnt) :
    global ans
    if i == goal :
        ans = cnt
        return

    calcu(i+1,goal,cnt+1)
    if ans != 0 :
        return
    calcu(i-1,goal,cnt+1)
    if ans != 0 :
        return
    calcu(i*2,goal,cnt+1)
    if ans != 0 :
        return
    calcu(i-10,goal,cnt+1)
    if ans != 0 :
        return



t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # 시작 자연수 N / 목표 자연수 M
    ans = 0                     # 최소 연산의 횟수를 담을 변수

    if N > M :
        a = 1
    else:
        a = 2

    calcu(N,M,0)

    print(f'#{tc} {ans}')
