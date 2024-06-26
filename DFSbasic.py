# swap

# def permutation(arr, r):    # r = 3
#     n = len(arr)
#     results = []
#     def _perm_swap(arr, depth):
#         if (depth == r):    # r = 3
#             results.append(arr[:r])
#             return
#         for i in range(depth, n):
#             arr[i], arr[depth] = arr[depth], arr[i]
#             _perm_swap(arr, depth+1)
#             arr[i], arr[depth] = arr[depth], arr[i]
#
#     _perm_swap(arr, 0)
#
#     return results
#
#
#
# print(permutation([1,2,3], 3))

# visited
#
# def permuation(arr, r):
#     n = len(arr)
#     visited = [False] * n
#     output = []
#     results = []
#
#     def _perm_visited(arr, visited, output, depth):
#         if(depth == r):
#             results.append(output[:])
#             return
#         for i in range(n):
#             if(visited[i]):
#                 continue
#
#             visited[i] = True
#             new_output = output+[arr[i]]
#
#             _perm_visited(arr, visited, new_output, depth+1)
#             visited[i] = False
#
#     _perm_visited(arr,visited,output, 0)
#
#     return results
#
# print(permuation([1,2,3], 3))


# recursion

def permutation(arr, r):
    result = []
    if r == 0:
        return [[]]

    for i in range(len(arr)):
        item = arr[i]
        for rest in permutation(arr[:i] + arr[i + 1:], r - 1):
            result.append([item] + rest)

    return result

print(permutation([1,2,2,4,3], 3))

# # 증복순열 *****

def permutation(arr, r):
    result = []
    arr.sort()  # 배열을 정렬하여 중복을 방지

    def generate_permutation(elements, r, path=[]):
        if r == 0:
            result.append(path)
            return

        for i in range(len(elements)):
            if i > 0 and elements[i] == elements[i - 1]:
                continue
            generate_permutation(elements[:i] + elements[i + 1:], r - 1, path + [elements[i]])

    generate_permutation(arr, r)
    return result


print(permutation([1, 2, 4, 3, 2], 3))

# def permutation2(arr, r):
#     n = len(arr)
#     output = []
#     results = []
#
#     def _perm(arr, output, depth, n, r):
#         if depth == r:
#             results.append(output[:])
#             return
#         for i in range(n):
#             new_output = output+[arr[i]]
#             _perm(arr, new_output, depth+1, n, r)
#     _perm(arr,output,0,n,r)
#
#     return results
# print(permutation2([1,2,3,2,2], 3))
#
