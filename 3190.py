
n = int(input())
board = [([0]*n) for i in range(n)]
numApple = int(input())
for i in range(numApple):
    x,y = map(int, input().split())
    board[x][y] = 1

#  → ↓ ← ↑
dx = [1, 0, -1, 0 ]
dy = [0, -1, 0, 1 ]
dir = 1
nx, ny = 0,0

L = int(input())
for i in range(L):
    when, dir = input().split()
    times[int(when)] = dir          #### times


# print(board)



time = 0
def go_snake():
    global time
    time += 1

Dummy = 1


numTurn = int(input())

for i in range(numTurn):
