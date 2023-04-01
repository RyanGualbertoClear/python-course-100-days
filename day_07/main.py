import random

word_list = ["cavalo", "camelo", "vaca", "boi", "avestruz", "papagaio",
             "pato", "galo", "galinha", "ganso", "peru", "pombo", "pavao"]
selected_word = word_list[random.choice(range(0, len(word_list)))]
masked_word = "_" * len(selected_word)
count_errors = 0

print("Bem vindo ao jogo da forca!")
print(f"A palavra tem {len(selected_word)} letras")


def print_masked_word(masked_word):
    print(masked_word)


def print_hugman(count_errors):
    if count_errors == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    elif count_errors == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       | \  ")
        print(" |       |  \ ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    elif count_errors == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |     / | \  ")
        print(" |    /  |  \ ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    elif count_errors == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |     / | \  ")
        print(" |    /  |  \ ")
        print(" |       |    ")
        print(" |        \   ")
        print("_|___      \  ")
        print()
    elif count_errors == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |     / | \  ")
        print(" |    /  |  \ ")
        print(" |       |    ")
        print(" |      / \   ")
        print("_|___  /   \  ")
        print()


while masked_word != selected_word and count_errors < 5:
    print_masked_word(masked_word)
    guess_letter = input("Digite uma letra: ").lower()
    for letter_index in range(0, len(selected_word)):
        letter = selected_word[letter_index]
        if letter == guess_letter:
            masked_word = masked_word[:letter_index] + letter + masked_word[letter_index + 1:]
            break
        else:
            if letter_index == len(selected_word) - 1:
                count_errors += 1
                print_hugman(count_errors)
                if count_errors == 5:
                    print("Você perdeu!")
                continue



if(masked_word == selected_word):
    print(f"Parabéns, você acertou a palavra era {selected_word}!")
