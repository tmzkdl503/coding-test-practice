'''
Title: 주식 가격
Type: 스택, 큐
Link: https://programmers.co.kr/learn/courses/30/lessons/42584
Reference: 스택/큐
'''

# 브루트포스로 해결

def solution(prices):
    ans = []
    
    for i in range(len(prices)):
        count = 0
        for j in range(i, len(prices)):
            if prices[i] <= prices[j]:
                if j == len(prices) - 1:
                    ans.append(count)
                else:
                    count += 1
            else:
                ans.append(count)
                break
                
    return ans
