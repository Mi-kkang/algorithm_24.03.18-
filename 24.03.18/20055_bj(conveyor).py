# 메모리 : 34184 KB / 시간 : 3936 ms

from collections import deque

N, K = map(int, input().split())        # 길이가 N인 컨베이어 벨트 / 내구도가 0인 칸의 개수 N
conveyor = deque(list(map(int, input().split())))   # 컨베이어 벨트 내구도 나타내는 덱
robot = deque([0] * (2*N))                                 # 로봇의 유무를 나타낼 덱

cnt = 0     # 회전 횟수를 넣을 변수

# print(conveyor)
# print(robot)

# 0) 시작하기 위해서는 일단 로봇이 존재해야 한다. / 넣고 시작하자 << 이 부분은 없어도 된다!
# robot[0] = 1
# conveyor[0] = conveyor[0] - 1
val_0 = conveyor.count(0)


while val_0 < K :  # 내구도가 0의 개수가 K개가 되기 전까지
    cnt += 1
    # 1) 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    conveyor.appendleft(conveyor.pop())
    robot.appendleft(robot.pop())
    robot[N-1] = 0

    # 2) 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    #   -> 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상 남아있어야 한다.
    # 2-1) 로봇이 존재하는 리스트를 찾는다. // 이 때, 위쪽 N까지만 올라가있는 부분이다. N 에서는 내려가야 하므로 N-1까지만 확인해도 괜찮다.
    ro_ex = []                  # 로봇이 있는 위치를 넣을 리스트
    for k in range(N-1) :
        if robot[k] == 1 :      # 로봇이 존재한다면,
            ro_ex.append(k)     # 로봇이 있는 위치 리스트에 넣기
    # 2-2) 얻은 리스트를 토대로 옆으로 이동할 수 있는지 확인해본다.
    ro_ex.sort(reverse=True)
    for l in ro_ex :
        if robot[l+1] == 0 and conveyor[l+1] >= 1 :  # 조건이 만족하면,
            robot[l] = 0
            robot[l+1] = 1
            conveyor[l+1] = conveyor[l+1] - 1

    robot[N-1] = 0  # 내리는 위치에 있는 로봇은 내린다.

    # 3) 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if conveyor[0] != 0 :
        robot[0] = 1
        conveyor[0] = conveyor[0] - 1

    val_0 = conveyor.count(0)
    if val_0 >= K :
        break


print(cnt)