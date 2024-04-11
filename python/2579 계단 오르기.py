# 게단은 한 번에 한 계단씩 또는 두 계단씩
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단 시작점은 계단x
# 마지막 도착 계단은 반드시 밟아야 한다.

n = int(input())

for _ in range(n):
    s = list(input())

sum = 0

for i in range(s):
    if s[i] < s[i+1] and s[i+1] < s[i+2]:
        sum += s[i+2]
    elif s[i] < s[i+1]:
        sum += s[i+1]
sum += s[-1]

print(sum)


