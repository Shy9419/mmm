# t = int(input())
#
# for _ in range(t):
n = int(input())
coins = list(map(int, input().split()))
coins.insert(0,0)
# a, b = map(int,input().split())
m = int(input())

dp = [[0] * (m+1) for i in range(n+1)]

print(dp)

