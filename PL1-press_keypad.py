'''
Title: 키패드 누르기
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/67256
Reference: 2020 카카오 인턴십
'''

def solution(numbers, hand):
    ans = ''
    
    # 패드 배열
    LPAD = [1, 4, 7, -1]
    MPAD = [2, 5, 8, 0]
    RPAD = [3, 6, 9, -1]
    
    # 엄지 포지션(행, 열)
    LP = [3, 0]
    RP = [3, 2]
    
    for num in numbers:
        
        if num in LPAD:
            LP = [LPAD.index(num), 0]
            ans += 'L'
        elif num in RPAD:
            RP = [RPAD.index(num), 2]
            ans += 'R'
        else:
            P = MPAD.index(num)
            if abs(P - LP[0]) + abs(1 - LP[1]) < abs(P - RP[0]) + abs(1 - RP[1]):
                LP = [P, 1]
                ans += 'L'
            elif abs(P - LP[0]) + abs(1 - LP[1]) > abs(P - RP[0]) + abs(1 - RP[1]):
                RP = [P, 1]
                ans += 'R'
            else:
                if hand == 'left':
                    LP = [P, 1]
                    ans += 'L'
                else:
                    RP = [P, 1]
                    ans += 'R'
    
    return ans
