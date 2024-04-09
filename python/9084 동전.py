import sys
input = sys.stdin.readline
# 입력값 받기
t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    coins.insert(0,0)
    m = int(input())
    # dp 테이블 만들기
    dp = [[0] * (m+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    # 값 비교 저장
    for j in range(1, n+1):
        for i in range(1, m+1):
            dp[j][i] = dp[j-1][i]
            if i-coins[j] >= 0:
                dp[j][i] += dp[j][i-coins[j]]
    print(dp[n][m])