x,y = 0,0
dir = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

## --> dir = 0 (0,1) dir = 1 (1,0)
## --> dir = 2 (0,-1) dir = 3 (-1,0)

nx, ny = x + dx[dir], y + dy[dir]
