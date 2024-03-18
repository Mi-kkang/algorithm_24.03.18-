N, L, R = map(int, input().split())     # NxN 크기의 땅 길이 N, 인구 차이가 L명 이상, R명 이하
nation = []
for _ in range(N) :
    con = list(map(int, input().split()))
    nation.append(con)

print(nation)