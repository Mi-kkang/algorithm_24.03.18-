def union(x, y) :       # 둘을 합져주자! 유니온 생성! (나 유니온 8000인데...)
    x = find_set(x)
    y = find_set(y)

    if x < y :          # 나는 그냥 작은 숫자에게 대표를 줬다!
        parents[y] = x
    else :
        parents[x] = y

def find_set(x) :           # 누구가 대표야! 찾아보자!
    if x == parents[x] :
        return x
    else :
        parents[x] = find_set(parents[x])
        return parents[x]

t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # N명의 사람 / 서로 알고 있는 관계 M개
    # relation = [[] for _ in range(N+1)]     # 사람의 수 +1 의 빈 리스트를 갖는 리스트 생성
    parents = [i for i in range(N+1)]       # make_set()과 같은 의미 / 자기 자신을 부모(유니온 대표)로 갖는 리스트 만들기

    for _ in range(M) :
        per1, per2 = map(int,input().split())

        # relation[per1].append(per2)  # 서로 알고 있기 때문에 양쪽을 다 연결해준다.
        # relation[per2].append(per1)

        union(per1,per2)

    cnt = 0     # 그룹의 개수를 셀 변수
    for i in range(1, N+1) :    # 우린 인덱스 1부터 사용했기 때문에 0부터 세면 안된다!!!
        if i == parents[i] :    # 인덱스 번호와 대표 번호가 같다면
            cnt += 1             # 1추가해준다!


    print(f'#{tc} {cnt}')