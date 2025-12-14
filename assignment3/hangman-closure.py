# pre-requisite: case-insensitive
def make_hangman(secret_word):
    guesses = []
    secret_word_lower = secret_word.lower()

    def hangman_closure(letter):
        guesses.append(letter.lower())
        to_print = []
        for secret_letter_lower in secret_word_lower:
            to_print.append(secret_letter_lower if secret_letter_lower in guesses else "_")
        print(f"Your current guess: {''.join(to_print)}")
        return not "_" in to_print
    return hangman_closure

user_input_secret_word = input("Please type a secret word (case-insensitive) " +
                               "or type 'exit' to exit: ")
print(user_input_secret_word)
secret_word = make_hangman(user_input_secret_word)
while(True):
    user_input_guess_letter = input("Please guess a letter: ").lower()
    if user_input_guess_letter == "exit":
        break
    if not len(user_input_guess_letter) == 1:
        print("Invalid input. Please enter only one character.")
        continue
    if secret_word(user_input_guess_letter):
        break
