def make_subset(i, value) :
    global cnt

    if value == K :     # 여태까지의 합이 목표 합과 같으면 카운트 늘리고 리턴
        cnt += 1
        return

    elif value > K :    # 여태까지의 합이 목표 합보다 크다면 그냥 리턴
        return

    elif i == N :       # 집합 인자들이 모두 선택이 다 되면 리턴
        return

    else :
        make_subset(i+1, value+arr[i])  # 현재 위치의 인자를 선택한다.
        make_subset(i+1, value)         # 선택 안한 채 간다.

t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, K = map(int,input().split())         # N개의 자연수 / 목표하는 합 K
    arr = list(map(int,input().split()))    # N개의 자연수 받기
    bit = [0] * N       # 비트를 쓸 예정! << 선택할지 / 안할지 (과연 비트가 필요한가?)
    cnt = 0             # 합이 K가 되는 부분집합의 개수를 넣을 변수

    make_subset(0, 0)

    print(f'#{tc} {cnt}')
