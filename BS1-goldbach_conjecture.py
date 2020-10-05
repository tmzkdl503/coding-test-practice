'''
Title: 골드바흐의 추측
Type: 구현, 수학
Link: https://www.acmicpc.net/problem/9020
Reference: 수학
'''

# 효율성을 높이기 위한 노력이 필요

import collections

t = int(input())
nums = [int(input()) for _ in range(t)]

n = max(nums)

eratos = [1 for _ in range(n + 1)]
eratos[0], eratos[1] = 0, 0

for i in range(2, int(n ** 0.5 + 1)):
    if eratos[i]:
        for j in range(i << 1, n + 1, i):
            eratos[j] = 0

for num in nums:
    entry = collections.deque()
    for i in range(num):
        if eratos[i] and eratos[num - i]:
            entry.appendleft((sorted([i, num - i]), abs(num-i-i)))

    print(' '.join(list(map(str, sorted(entry, key=lambda x: x[1])[0][0]))))
