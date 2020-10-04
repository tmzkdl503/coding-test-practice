'''
Title: 큰 수 만들기
Type: 그리디
Link: https://programmers.co.kr/learn/courses/30/lessons/42883
Reference: 탐욕법
'''

# 스택에 저장하면서 더 큰 수가 나오면 기존 것을 버리고 새 것을 취하는 방법

def solution(number, k):
    st = []
    
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
        
    return ''.join(st[:len(st) - k])
