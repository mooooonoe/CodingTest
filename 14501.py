day = int(input())
T = [0]*day
P = [0]*day

for i in range(day):
    a, b = map(int,input().split())
    T[i] = a; P[i]=b

max_value = 0
dp = [0]*(day+1)

for i in range(day-1, -1, -1):
    if T[i] <= (day-i):
            dp[i] = max(P[i]+dp[i+T[i]], max_value)
            max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
