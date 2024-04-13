N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

max = N*M
cnt = 0
xy = [0]*max; num = [0]*max

# 북 동 남 서
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
#
# def saw(num, board):
#     rect = board
#     if i == 1:
#         now = xy[cnt]
#         for len()
#         x = dx[dir]; y = dy[dir]
#
#     elif i == 2:
#
#     elif i == 3:
#
#     elif i == 4:
#
#     elif i == 5:
#
#     return result
#
# for i in range(N):
#     for j in range(M):
#         if board[i][j] != 0:
#             xy[cnt] = [i,j]
#             num[cnt] = board[i][j]
#             cnt += 1

result = board.count(0)

print(result)
#
# xy = xy[:cnt]
# num = num[:cnt]
#
# min = N*M
# for i in num:
#
#     for _ in 4:
#
#         result = saw(i, board)
#
#         if result < min:
#             min = result
#         else:
#             continue
#
# print(min)



