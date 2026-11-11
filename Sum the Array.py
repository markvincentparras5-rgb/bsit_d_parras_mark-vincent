def sum_array(arr, i=0):
    if i == len(arr):
        return 0

    return arr[i] + sum_array(arr, i + 1)


print("1. SUM THE ARRAY")
print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4, 5]))
print(sum_array([-2, 5, -3, 10]))