'''
Title: 문자열 압축
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/60057
Reference: 2020 KAKAO BLIND RECRUITMENT
'''

def solution(s):
    anslist = set()
    
    for i in range(1, len(s)+1):
        tmp = []
        tmp2 = []
        for j in range(0, len(s), i):
            tmp.append(s[j:j+i])
            
        now = ''
        count = 0
        for k, tok in enumerate(tmp):
            if not now:
                now = tok
                count += 1
                if k == len(tmp) - 1: # 마지막이면 더해줌
                    tmp2.append(now + (str(count) if count > 1 else ''))
            else:
                if tok == now:
                    count += 1
                else:
                    tmp2.append(now + (str(count) if count > 1 else ''))
                    count = 1
                    now = tok
                if k == len(tmp) - 1: # 마지막이면 더해줌
                    tmp2.append(tok + (str(count) if count > 1 else ''))
                    
        anslist.add(len(''.join(tmp2)))

    return min(anslist)
