import sys
S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
print(matrix[-1][-1])

# if i == 0 or j == 0:    # 마진 설정
#     LCS[i][j] = 0
# elif string_A[i] == string_B[j]:
#     LCS[i][j] = LCS[i - 1][j - 1] + 1   # 두 문자가 같다면 LCS[i - 1][j - 1] 값을 찾아 + 1 한다.
# else:
#     LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])   # 두 문자가 다르다면 LCS[i - 1][j], LCS[i][j - 1] 중에 큰 값을 표시한다.
