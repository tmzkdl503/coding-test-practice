'''
Title: 네번째 점
Type: 구현, 비트 연산
Link: https://www.acmicpc.net/problem/3009
Reference: 수학
'''

# x, y 각각에 대해 짝이 맞지 않는(홀수 번 등장하는) 좌표값이 정답, 같은 수를 xor하면 상쇄되는 원리를 활용

x, y = 0, 0

for _ in range(3):
    a, b = list(map(int, input().split()))
    x ^= a
    y ^= b
    
print(x, y)
