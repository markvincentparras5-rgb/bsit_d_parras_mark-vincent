def find_largest(arr, i=0):
    if len(arr) == 0:
        raise ValueError("Array must not be empty.")

    if i == len(arr) - 1:
        return arr[i]

    largest_rest = find_largest(arr, i + 1)

    if arr[i] > largest_rest:
        return arr[i]
    else:
        return largest_rest


print("\n2. FIND THE LARGEST NUMBER")
print(find_largest([8]))
print(find_largest([10, 5, 3, 2]))
print(find_largest([1, 2, 3, 15]))
print(find_largest([-10, -5, -2, -8]))