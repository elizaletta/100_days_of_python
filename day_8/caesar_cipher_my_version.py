alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            output_text += new_letter
        elif cipher_direction == "decode":
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            output_text += new_letter
    print(f"The text is {output_text}")

caesar(input_text=text, shift_amount=shift, cipher_direction=direction)