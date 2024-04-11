# 각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다.
# 반드시 오른쪽이나 아래쪽으로만 이동해야 한다.
# 0은 더 이상 진행을 막는 종착 점이다.
# 한 번 점프를 할 때, 방향을 바꾸면 안 된다.
# 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.

n = int(input())


for _ in range(n):
    a,b,c,d = map(int, input().split())


t = [[0] * (n) for _ in range(n)]
c = 0


for i in range(n):
    for j in range(n):




