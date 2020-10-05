'''
Title: 베르트랑 공준
Type: 수학
Link: https://www.acmicpc.net/problem/4948
Reference: 수학
'''

# 경계값을 잘 파악하기

while True:
    n = int(input())
    if not n:
        break

    eratos = [1 for _ in range((n << 1) + 1)]
    eratos[0], eratos[1] = 0, 0

    for i in range(2, int((n << 1) ** 0.5) + 1):
        if eratos[i]:
            for j in range(i << 1, (n << 1) + 1, i):
                eratos[j] = 0

    ans = 0
    for i in range(n + 1, (n << 1) + 1):
        ans += eratos[i]

    print(ans)
