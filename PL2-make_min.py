'''
Title: 최솟값 만들기
Type: 그리디
Link: https://programmers.co.kr/learn/courses/30/lessons/12941
Reference: 연습문제
'''

# 한 배열의 최솟값과 다른 배열의 최댓값을 곱해나가는 방식
# A 내림차순, B 오름차순으로 수행해도 같은 결과가 나온다(앞 뒤만 바뀜)

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    x = 0
    for a, b in zip(A, B):
        x += a * b
        
    return x
