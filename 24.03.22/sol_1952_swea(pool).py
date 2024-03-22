def f(i, s) :       # i월까지 비용을 계산하는 함수 / s는 비용
    global min_v
    global cnt
    cnt += 1
    if i > 12 :
        if min_v > s :
            min_v = s

    elif s >= min_v :
        return

    else :
        f(i+1, s + min(days[i]*day, month))     # i월만 결제
        f(i+3, s + month3)                      # i월부터 3개월분 결제


t = int(input())

for tc in range(1, t+1) :
    day, month, month3, year = map(int, input().split())

    days = [0] + list(map(int,input().split()))   # 월별 이용일 수 days[i]

    min_v = year    # 1년치를 한번에 결제하는 비용
    cnt = 0
    f(1, 0)

    print(f'#{tc} {min_v}')