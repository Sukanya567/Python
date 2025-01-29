def char_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_string = input("Enter a string: ")
frequency = char_frequency(input_string)
print("Character frequencies:")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")
