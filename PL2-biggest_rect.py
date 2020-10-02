'''
Title: 가장 큰 정사각형 찾기
Type: 다이나믹 프로그래밍
Link: https://programmers.co.kr/learn/courses/30/lessons/12905
Reference: 연습문제
'''

# 2x2를 돌면서 오른쪽 아래칸이 0보다 크면 나머지 3칸 중 최솟값 + 1을 오른쪽 아래칸에 넣어주는 방식
# 오른쪽 아래값을 max랑 비교해서 항상 넣어줌(각 케이스의 오른쪽 아랫값은 만들수있는 정사각형의 한 변의 길이가 됨)

def solution(board):
    answer = 1234

    row = len(board)
    col = len(board[0])
    
    if row == 1 or col == 1:
        return 1
    
    maxi = 0
    for i in range(row-1):
        for j in range(col-1):
            if board[i+1][j+1] > 0:
                board[i+1][j+1] = min(board[i][j], board[i+1][j], board[i][j+1]) + 1
                maxi = max(maxi, board[i+1][j+1])
    
    pprint.pprint(board)
    
    return maxi**2
