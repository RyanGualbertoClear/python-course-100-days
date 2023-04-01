alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

loop_on = True


def encrypt(text, shift):
    if (direction == "encode"):
        cipher_text = ""
        for letter in text:
            letter_index_in_alphabet = alphabet.index(letter)
            cipher_letter_index = letter_index_in_alphabet + shift
            cipher_text += alphabet[cipher_letter_index]
        print(f"here's the encoded result: {cipher_text}")
    if (direction == "decode"):
        decode_text = ""
        for letter in text:
            letter_index_in_alphabet = alphabet.index(letter)
            cipher_letter_index = letter_index_in_alphabet - shift
            decode_text += alphabet[cipher_letter_index]
        print(f"here's the decoded result: {decode_text}")


while loop_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text=text, shift=shift)
    loop_on = input("Type 'Yes' if you want go again. Otherwise type 'no'. ").lower() == "yes"
print("GoodBye")