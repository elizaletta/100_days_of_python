from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        else:
            output_text += char
            
    print(f"The {cipher_direction}d text is {output_text}")

print(logo)

answer = "yes"
while answer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" or direction != "decode":
         print("Oops, there's a mistake.")
         direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    answer = str(input("Do you want to start again? Type 'yes' if you want to go again and 'no' if you want to quit:\n").lower())
print("Goodbye")