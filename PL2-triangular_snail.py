'''
Title: 삼각 달팽이
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/68645
Reference: 월간 코드 챌린지 시즌1
'''

# 시뮬레이션을 통해 규칙을 찾고 규칙대로 구현

import itertools

def solution(n):
    magic = [[0 for _ in range(n)] for _ in range(n)]
    count = [n-i for i in range(n)]
    
    # 0. i++
    # 1. j++
    # 2. i--, j--
    mode = -1
    numb = 0
    pos = [-1, 0]
    for c in count:
        mode += 1
        for i in range(c):
            if mode % 3 == 0: # i++
                numb += 1
                pos = [pos[0] + 1, pos[1]]
                magic[pos[0]][pos[1]] = numb
            elif mode % 3 == 1: # j++
                numb += 1
                pos = [pos[0], pos[1] + 1]
                magic[pos[0]][pos[1]] = numb
            elif mode % 3 == 2: # i--, j--
                numb += 1
                pos = [pos[0] -1, pos[1] -1]
                magic[pos[0]][pos[1]] = numb
    
    remagic = [x[:i+1] for i, x in enumerate(magic)]

    return list(itertools.chain(*remagic))
