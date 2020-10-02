'''
Title: 방금그곡
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/17683
Reference: 2018 KAKAO BLIND RECRUITMENT [3차]
'''

def time2min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(m, musicinfos):
    # 샾 붙은거 한 글자로 변환하기 => replace 함수로
    sharp = {
        'A#': 'a',
        'B#': 'b',
        'C#': 'c',
        'D#': 'd',
        'E#': 'e',
        'F#': 'f',
        'G#': 'g',
    }    
    
    # 변환 끝
    for s in sharp.keys():
        m = m.replace(s, sharp[s])
        
    ans = []    
    
    # 음악 정보 파싱
    for mu in musicinfos:
        st, ed, title, melo = mu.split(',')
        st = time2min(st)
        ed = time2min(ed)
        dur = ed - st
        
        for s in sharp.keys():
            melo = melo.replace(s, sharp[s])
        
        newmelo = ''
        for i in range(dur):
            newmelo += melo[i % len(melo)]
            
        if m in newmelo:
            ans.append((dur, title))
            
    if not ans:
        return '(None)'
    else:
        ans.sort(key=lambda x: x[0], reverse=True)
        return ans[0][1]
