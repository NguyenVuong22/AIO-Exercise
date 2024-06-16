def max_kernel(num_list, k):
    result = []
    res = []
    a = 0
    while ((k + a) <= len(num_list)):
        for i in range(a, k + a):
            res.append(num_list[i])
        result.append(max(res))
        a = a + 1
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
