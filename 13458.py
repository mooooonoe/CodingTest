N = int(input())

tester = list(map(int, input().split()))

a, b = map(int, input().split())

total = N
for i in tester:
    i -= a
    if i > 0:
        if i % b:
            total += (i//b) +1
        else:
            total += (i//b)

print(total)