def rearrange_alternatively(arr, n):
    result = [0] * n
    max_index = n - 1
    min_index = 0
    is_max_turn = True

    for i in range(n):
        if is_max_turn:
            result[i] = arr[max_index]
            max_index -= 1
        else:
            result[i] = arr[min_index]
            min_index += 1
        is_max_turn = not is_max_turn
    return result
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
rearranged_array = rearrange_alternatively(arr, n)
print("Rearranged array:", rearranged_array)
