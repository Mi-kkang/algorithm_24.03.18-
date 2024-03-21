def find_set(x) :
    if parents[x] == x :
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y) :
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이면 리턴
    if x == y :
        return

    if x < y :
        parents[y] = x

    else :
        parents[x] = y


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    V, E = map(int,input().split())     # 노드 번호 V / 간선의 개수 E
    edges = []      # 간선 정보를 저장할 리스트

    for _ in range(E) :
        s, e, w = map(int, input().split())     # 시작점 s / 끝점 e / 가중치 w
        edges.append([s,e,w])                   # 간선 정보 저장

    edges.sort(key=lambda x : x[2])     # 가중치를 기준으로 정렬
    parents = [i for i in range(V+1)]     # 대표자 만들기 / 본인을 가리킴 << 1부터 시작이라 V+1로 인덱스 만들어주기

    ans = 0     # 가중치를 저장할 변수
    cnt = 0     # MST 완성 : 간선의 개수가 V-1일 때

    for s,e,w in edges :

        # 사이클이 발생한다 / 이미 연결되어 있다! 건너뛰기
        if find_set(s) == find_set(e) :
            continue

        # 사이클이 없다면, 같은 유니온으로 묶어주자
        union(s,e)
        ans += w        # 가중치 추가해주기

        if cnt == V-1 :     # 완성되면 탈출출
           break

    print(f'#{tc} {ans}')