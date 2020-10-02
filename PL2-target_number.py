'''
Title: 타겟 넘버
Type: 탐색
Link: https://programmers.co.kr/learn/courses/30/lessons/43165
Reference: 연습문제
'''



# 다른 풀이(dfs보다 2배정도 빠름)
def solution(numbers, target):
    
    anslist = [0]
    for i in numbers:
        tmplist = []
        for a in anslist:
            tmplist.append(a+i)
            tmplist.append(a-i)
        anslist = tmplist
    
    return anslist.count(target)
    

# dfs를 활용한 풀이
answer = 0
g_numbers = []
g_target = 0


def dfs(value, count):
    global answer, g_numbers, g_target
    
    if count == len(g_numbers) - 1:
        if value == g_target:
            answer += 1
        return
    
    count += 1
    dfs(value + g_numbers[count], count)
    dfs(value - g_numbers[count], count)

def solution(numbers, target):
    global answer, g_numbers, g_target
    g_numbers, g_target = numbers, target
    
    dfs(g_numbers[0], 0)
    dfs(-g_numbers[0], 0)
    
    return answer
