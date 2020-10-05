'''
Title: 소수 찾기
Type: 수학
Link: https://www.acmicpc.net/problem/1978
Reference: 수학
'''

n = int(input())
numb = list(map(int, input().split()))

maxi = max(numb)

# n이 최댓값이 아니므로 maxi를 기준으로 에라토스테네스의 체를 수행해야 함
eratos = [1 for _ in range(maxi + 1)]
eratos[0], eratos[1] = 0, 0
for i in range(2, int(maxi ** 0.5) + 1):
    if eratos[i] == 1:
        for j in range(i * 2, maxi + 1, i):
            eratos[j] = 0

ans = 0
for num in numb:
    ans += eratos[num]

print(ans)
