# import cipher_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
check = "yes"
while check == "yes":
    direction = input("Type 'encode to encrypt, type 'decode to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    def ceasar(combined_text, combined_shift, cippher_direction):
        cippher = ""
        for letter in combined_text:
            if letter in combined_text:
                position = alphabet.index(letter)
                if cippher_direction == "encode":
                    new_position = position + combined_shift
                elif cippher_direction == "decode":
                    new_position = position - combined_shift
                new_letter = alphabet[new_position]
                cippher += new_letter
            else:
                cippher += letter
        print(f"The {cippher_direction}ed text is {cippher}")
        check = input('Type "yes" if you want to go again. Otherwise type "no". ')

    ceasar(text, shift, direction)
