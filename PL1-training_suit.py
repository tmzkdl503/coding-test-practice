'''
Title: 체육복
Type: 그리디
Link: https://programmers.co.kr/learn/courses/30/lessons/42862
Reference: 탐욕법(Greedy)
'''

def solution(n, lost, reserve):
    clothes = [1 for i in range(n)]
    
    for lo in lost:
        clothes[lo-1] -= 1
        
    for re in reserve:
        clothes[re-1] += 1
        
    for i, c in enumerate(clothes): # 한쪽에만 빌려줄 수 있는 사람 먼저 빌려주기
        if c == 2 and ((i != 0 and i != n-1 and clothes[i-1] + clothes[i+1] != 0) or i == 0 or i == n-1):
            if i != 0 and clothes[i-1] == 0:
                clothes[i-1] += 1
                clothes[i] -= 1
                continue
            elif i != n-1 and clothes[i+1] == 0:
                clothes[i+1] += 1
                clothes[i] -= 1
                continue
    
    for i, c in enumerate(clothes): # 나머지는 왼쪽부터 빌려주기
        if c == 2:
            if i != 0 and clothes[i-1] == 0:
                clothes[i-1] += 1
                clothes[i] -= 1
                continue
            elif i != n-1 and clothes[i+1] == 0:
                clothes[i+1] += 1
                clothes[i] -= 1
                continue
    
    return len([x for x in clothes if x > 0])
