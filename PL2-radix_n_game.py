'''
Title: N진수 게임
Type: 구현, 
Link: https://programmers.co.kr/learn/courses/30/lessons/17687
Reference: 2018 KAKAO BLIND RECRUITMENT [3차]
'''

def solution(n, t, m, p):
    sym = '0123456789ABCDEF'
    table = ''
    ans = ''
    
    # 1. 전체 정답 테이블을 구성
    for i in range(t * m):
        tmp = ''
        
        a, b = i, n
        
        while True:
            d, r = divmod(a, b)
            tmp += sym[r]
            if d != 0:
                a = d
            else:
                break
        
        table += tmp[::-1]
    
    # 2. 말해야 할 것들만 뽑아냄
    for i in range(p - 1, len(table), m):
        ans += table[i]
        if len(ans) >= t:
            break
        
    return ans
