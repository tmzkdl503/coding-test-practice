'''
Title: 2016년
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12901
Reference: 연습문제
'''

# 다른 풀이 방법으로는 {월: 날짜 수} 딕셔너리를 활용해 총 날짜 % 7을 인덱스로 활용하는 방법도 있음

# 둠스데이 알고리즘 적용
def solution(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    doomsday = [4, 29, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    step = b - doomsday[a-1]
    
    return day[(1 + step) % 7]
