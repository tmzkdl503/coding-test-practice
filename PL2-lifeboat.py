'''
Title: 구명보트
Type: 그리디
Link: https://programmers.co.kr/learn/courses/30/lessons/42885
Reference: 탐욕법
'''

def solution(people, limit):
    people.sort(reverse=True)
    
    st = 0
    ed = len(people) - 1
    
    ans = 0
    
    while st < ed:
        if people[st] + people[ed] <= limit: # 가장 큰 사람과 작은 사람이 한 보트에 탈 수 있으면 보낸다
            ans += 1
            st += 1
            ed -= 1
        else: # 함께 탈 수 없다면
            # 가장 큰 사람은 혼자 타야 하니 보낸다
            ans += 1
            st += 1
    if st == ed: # 남은 한 사람을 보낸다
        ans += 1
            
    return ans
