def encode_string(input_string, shift):
    encoded_string = ""
    for char in input_string:
        encoded_string += chr(ord(char) + shift)
    return encoded_string
input_string = input("Enter a string: ")
shift = int(input("Enter a number to encode the string: "))
encoded_string = encode_string(input_string, shift)
print("Encoded string:", encoded_string)
