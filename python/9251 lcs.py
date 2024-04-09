import sys
input = sys.stdin.readline

string_A = [0] + list(input().rstrip())     # 문자열 입력값을 받는다.
string_B = [0] + list(input().rstrip())

dp = [[0] * len(string_B) for _ in range(len(string_A))]    # dp를 초기화한다.

for i in range(1, len(string_A)):   # 2차원 배열을 반복
    for j in range(1, len(string_B)):
        if string_A[i] == string_B[j]:  # 만약 같다면
            dp[i][j] =dp[i-1][j-1]+ 1   # 2차원 배열에 1을 더해서 표시
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])  # 그렇지 않다면(다르다면) 그 순간까지의 최대값을 가져옴.

print(dp[len(string_A) - 1][len(string_B) - 1])
