n, m, x, y, k = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

nx = x; ny = y

rect = [0]*6
def turn(dir):
    a, b, c, d, e, f = rect[0], rect[1], rect[2], rect[3], rect[4], rect[5]
    if dir == 0:
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = d, b, a, f, e, c
    elif dir == 1:
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = c, b, f, a, e, d
    elif dir == 2:
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = e, a, c, d, f, b
    else :
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = b, f, c, d, a, e

    return rect

comm = list(map(int, input().split()))

for i in comm:
    nx += dx[i-1]
    ny += dx[i-1]

    turn(dir)



    if board[nx][ny]  == 0:
        board[nx][ny]  = rect[-1]

    else :
        rect[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(rect[0])


