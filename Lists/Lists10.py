def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = insertion_sort(numbers)
print("Sorted list:", sorted_numbers)
