t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1,t+1) :
    N = int(input())        # NxN 방의 길이 N
    room = [list(map(int,input().split())) for _ in range(N)]   # 방을 받는다.
    check = [0] * (N*N + 1)     # 인덱스 번호 방 주변에 +1 방이 있는지 확인하기 위한 리스트

    for i in range(N) :     # 방을 다 돌면서
        for j in range(N) :

            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :     # 상하좌우를 다 보면서,
                ni = i + di
                nj = j + dj

                if 0<=ni<N and 0<=nj<N and room[ni][nj] == room[i][j] + 1 : # 주변에 자신의 숫자보다 +1인 방이 있다면,
                    check[room[i][j]] = 1   # 자신의 인덱스 번호에 1을 저장해준다.


    max_v = 0     # 최대의 연속된 1의 개수(순서대로 방을 이동할 수 있는 수 -1)을 저장할 예정
    room_n = 0    # 이동을 제일 많이 할 수 있는 방 번호를 저장할 예정(같은 이동 숫자면 작은 방번호가 들어가야 함)
    cnt = 0       # 이동할때마다 연속된 1의 개수를 세 줄 예정(0을 만나면 초기화 가능)

    for k in range(N*N+1) :

        if check[k] == 1 :
            cnt += 1

        if check[k] == 0 :
            if max_v < cnt :
                max_v = cnt
                room_n = k-cnt  # 나는 앞에서부터 확인했기 때문에 cnt 만큼 빼줘야 방 번호가 나온다...

            cnt = 0


    print(f'#{tc} {room_n} {max_v+1}')