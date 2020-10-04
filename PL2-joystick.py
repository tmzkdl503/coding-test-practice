'''
Title: 조이스틱
Type: 구현, 그리디
Link: https://programmers.co.kr/learn/courses/30/lessons/42860
Reference: 탐욕법
'''

def solution(name):  
    magic = {}
    ans = 0
    
    # 상하 이동 수를 미리 구축 magic
    val = -1
    add = 1
    for i in range(26):
        val += add
        if val == 13:
            add = -1
        magic[chr(ord('A') + i)] = val
    
    todo = [(1 if x != 'A' else 0) for x in name]
    
    pos = 0
    while sum(todo) != 0:
        if todo[pos] == 1:
            ans += magic[name[pos]]
            todo[pos] = 0
        else:
            move = 0
            while True:
                move += 1
                left = todo[(pos-move) % len(todo)]
                right = todo[(pos+move) % len(todo)]
                
                if left == 1 == right == 1:
                    lsum = 0
                    rsum = 0
                    if (pos - move) % len(todo) < pos:
                        lsum = sum(todo[(pos - (len(todo) // 2)) % len(todo):pos])
                    else:
                        lsum = sum(todo[:pos] + todo[(pos - (len(todo) // 2)) % len(todo):])
                    if (pos + move) % len(todo) > pos:
                        rsum = sum(todo[pos+1:(pos + (len(todo) // 2)) % len(todo)+1])
                    else:
                        rsum = sum(todo[pos:] + todo[:(pos + (len(todo) // 2)) % len(todo)+1])
                    if lsum <= rsum:
                        pos = (pos - move) % len(todo)
                        ans += move
                        break
                    else:
                        pos = (pos + move) % len(todo)
                        ans += move
                        break
                elif left == 1:
                    pos = (pos - move) % len(todo)
                    ans += move
                    break
                elif right == 1:
                    pos = (pos + move) % len(todo)
                    ans += move
                    break
                elif move > len(todo):
                    return -1
    
    return ans
