'''
Title: 직사각형에서 탈출
Type: 수학
Link: https://www.acmicpc.net/problem/1085
Reference: 수학
'''

# 상하좌우 체크

x, y, w, h = list(map(int, input().split()))
print(min(x, y, w - x, h - y))
