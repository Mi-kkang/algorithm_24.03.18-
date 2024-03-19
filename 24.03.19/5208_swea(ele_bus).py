def move_bus(i,ch) :      # i : 지금 몇번째 정류장인가? / ch : 몇 번 배터리를 변경했나?
    global min_v
    if ch >= min_v :
        return

    if i >= end :
        if min_v > ch :
            min_v = ch

        return

    for k in range(1, M[i]+1) :
        move_bus(i+k, ch+1)



t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, *M = map(int, input().split())   # 정류장 수 N / 정류장 별 배터리 개수

    start = M[0]    # 처음 충전한 배터리 용량
    min_v = N       # 최소 교체 횟수를 담을 변수 / 초기값을 최대인 N으로 만들었다(N 이상이 나올 수 없음)
    end = len(M)

    move_bus(0, 0)

    print(f'#{tc} {min_v-1}')

