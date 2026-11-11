def count_number(arr, target, i=0):
    if i == len(arr):
        return 0

    if arr[i] == target:
        return 1 + count_number(arr, target, i + 1)
    else:
        return count_number(arr, target, i + 1)


print("\n3. COUNT A CHOSEN NUMBER")
print(count_number([], 5))
print(count_number([2, 5, 5, 3, 5], 5))
print(count_number([1, 2, 3, 4], 7))