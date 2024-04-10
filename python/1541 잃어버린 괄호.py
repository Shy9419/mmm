# 입력값
exp = input().split('-')
ans = 0
# exp 에 0번 값에 +를 기준으로 스플릿
for i in exp[0].split('+'):
    ans += int(i)

for i in exp[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)