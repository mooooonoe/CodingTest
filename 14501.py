day = int(input())
T = [0]*day; P = [0]*day

for i in range(day):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

dp = [0]*(day+1)
max_val = 0

for i in range(day-1, -1, -1):
    if T[i]+i <= day:
        dp[i] = max(P[i]+dp[i+T[i]], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)


