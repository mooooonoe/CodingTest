row, col, x, y, k = map(int, input().split())

# 동 서 남 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
rect = [0,0,0,0,0,0]

def turn(dir):
    a, b, c, d, e, f = rect[0], rect[1], rect[2], rect[3], rect[4], rect[5]
    if dir == 1:
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = d, a, c, d, e, f
    elif dir == 2:  # 서
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = b, c, d, a, e, f
    elif dir == 3:  # 북
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = e, b, f, d, c, a
    else:
        rect[0], rect[1], rect[2], rect[3], rect[4], rect[5] = f, b, e, d, a, c

board = []

for i in range(row):
    board.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

nx, ny = x, y

for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= row or ny < 0 or ny >= col:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)

    if board[nx][ny] == 0:
        board[nx][ny] = rect[2]
    else:
        rect[2] = board[nx][ny]
        board[nx][ny] = 0

    print(rect[0])


