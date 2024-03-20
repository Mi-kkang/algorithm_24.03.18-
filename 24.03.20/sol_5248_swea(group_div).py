def find_set(x) :
    while x != p[x]:    # 자기 자신을 가리키면(p[x]==x) 대표원소
        x = p[x]
    return x

def union(a, b) :   # b의 대표원소가 자기자신 대신 a의 대표원소를 가리키도록 바꿈
    # 금지
    # p[b] = a
    # p[b] = find_set(a)
    p[find_set(b)] = find_set(a)


def find_set_r(x) : # 참고
    if x == p[x] :
        return x
    else :
        p[x] = find_set_r(p[x])   # path compression
        return p[x]
        # 아닌 버전은 그냥 리턴만
        # return find_set_r(p[x])


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())        # N번 까지의 출석번호 / M 장의 신청서
    arr = list(map(int, input().split()))   # M 쌍의 번호 받기

    p = [i for i in range(N+1)]     # 각자 대표원소 make_set(1) ~ make_set(N)

    for i in range(M) :
        a, b = arr[i*2], arr[i*2+1]
        union(a, b)

    cnt = 0
    for i in range(1, N+1) :
        if i == p[i] :          # 대표원소인 경우
            cnt += 1            # 대표원소 개수 == 그룹의 수

    print(f'#{tc} {cnt}')