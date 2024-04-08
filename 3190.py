n = int(input())
board = [([0]*n) for _ in range(n)]

k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    board[x-1][y-1] = 2

L = int(input())
times = [0]*10000
for _ in range(L):
    when,dirct = input().split()
    times[int(when)] = dirct

snake=[]
snake.append([0,0])
board[0][0] = 1

# 위 오른쪽 아래 왼쪽
# 0     1  2    3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dirct = 1

nx,ny = 0,0

time = 0

while(True):
    time += 1
    nx = nx + dx[dirct]
    ny = ny + dy[dirct]

    if(nx<0 or ny<0 or nx>=n or ny>=n or board[nx][ny]==1):
        break

    if(board[nx][ny] == 2):
        snake.append([nx,ny])
        board[nx][ny] = 1

    elif(board[nx][ny] == 0):
        snake.append([nx,ny])
        board[nx][ny] = 1

        delX,delY = snake.pop(0) # 처음 시작한 꼬리 비우기
        board[delX][delY] = 0

    if(times[time] =='D'):
        dirct = (dirct + 1) % 4
    elif(times[time] =='L'):
        dirct = (dirct + 3) % 4

print(time)


