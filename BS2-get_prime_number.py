'''
Title: 소수 구하기
Type: 수학
Link: https://www.acmicpc.net/problem/1929
Reference: 수학
'''

m, n = list(map(int, input().split()))

eratos = [1 for _ in range(n + 1)]
eratos[0], eratos[1] = 0, 0

for i in range(2, int(n ** 0.5) + 1):
    if eratos[i]:
        for j in range(i << 1, n + 1, i):
            eratos[j] = 0

for i in range(m, n + 1):
    if eratos[i]:
        print(i)
