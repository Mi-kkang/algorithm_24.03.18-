t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())        # N번 까지의 출석번호 / M 장의 신청서
    arr = list(map(int, input().split()))   # M 쌍의 번호 받기