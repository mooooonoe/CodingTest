N = int(input())
num = list(map(int, input().split()))
tools = list(map(int, input().split()))
dtool = [0, 1, 2, 3] # +  -  *  /
org = [0]*(N-1); cnt=0

for i in range(4):
    while(tools[i]>0):
        org[cnt] = dtool[i]
        cnt += 1
        tools[i] -= 1
    if(tools[i]==0):
        continue

print(org)
#
# global minResult
# global maxResult
#
# minResult = -1e9
# maxResult = 1e9
#
#
# def permutation(arr, r):
#     result = []
#     arr.sort()
#     def gen_permutation(elements, r, path=[]):
#         if r == 0:
#             result.append(path)
#             return
#
#         for i in range(len(elements)):
#             if i > 0 and elements[i] == elements[i-1]:
#                 continue
#             gen_permutation(elements[:i]+elements[i+1:], r - 1, path + [elements[i]])
#
#     gen_permutation(arr,r)
#     return result
#
# # print(permutation([1, 2, 4, 3, 2], 3))
#
# class ToolMath:
#     def plustool(a,b) -> int:
#         return a+b
#     def minustool(a,b) -> int:
#         return a-b
#     def multitool(a,b) -> int:
#         return a*b
#     def devitool(a,b) -> int:
#         return a/b
#
#
#
# for _ in range(num):
#
#     tool(num(N),num(N+1), ())


