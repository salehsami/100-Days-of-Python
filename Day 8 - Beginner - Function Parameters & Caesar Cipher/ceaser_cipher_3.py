alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode to encrypt, type 'decode to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def ceasar(combined_text, combined_shift, cippher_direction):
    cippher = ""
    for letter in combined_text:
        position = alphabet.index(letter)
        if cippher_direction == "encode":
            new_position = position + combined_shift
        elif cippher_direction == "decode":
            new_position = position - combined_shift
        new_letter = alphabet[new_position]
        cippher += new_letter
    print(f"The {cippher_direction}ed text is {cippher}")


ceasar(text, shift, direction)
