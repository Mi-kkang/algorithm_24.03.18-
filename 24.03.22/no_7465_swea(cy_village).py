def make_group() :
    pass


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # N명의 사람 / 서로 알고 있는 관계 M개
    relation = [[] for _ in range(N+1)]     # 사람의 수 +1 의 빈 리스트를 갖는 리스트 생성
    parents = [i for i in range(N+1)]       # make_set()과 같은 의미 / 자기 자신을 부모(유니온 대표)로 갖는 리스트 만들기

    for _ in range(M) :
        per1, per2 = map(int,input().split())

        relation[per1].append(per2)     # 서로 알고 있기 때문에 양쪽을 다 연결해준다.
        relation[per2].append(per1)


    make_group(1)