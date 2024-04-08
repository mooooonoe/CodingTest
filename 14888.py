N = int(input())
num = [list(map(int, input().split())) for i in range(N)]

plus, minus, multi, devi = map(int, input().split())

        # +  -  *  /
dtool = [0, 1, 2, 3]

global minResult = -1e9
global maxResult = 1e9

def plustool(a,b) -> int:
    return a+b
def minustool(a,b) -> int:
    return a-b
def multitool(a,b) -> int:
    return a*b
def devitool(a,b) -> int:
    return a/b

for _ in range(N):

    tool(num(N),num(N+1), ())