'''
Title: 소수
Type: 수학
Link: https://www.acmicpc.net/problem/2581
Reference: 수학
'''

# 세부 사항을 헷갈리지 말 것

m = int(input())
n = int(input())

eratos = [1 for _ in range(n + 1)]
eratos[0], eratos[1] = 0, 0

for i in range(2, int(n ** 0.5) + 1):
    if eratos[i]:
        for j in range(i << 1, n + 1, i):
            eratos[j] = 0

ans = 0
flag = 1
mini = float('-inf')
for i in range(m, n + 1):
    if eratos[i]:
        ans += i
        if flag:
            mini = i
            flag = 0

if not ans:
    print(-1)
else:
    print(ans)
    print(mini)
