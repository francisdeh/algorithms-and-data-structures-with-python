import random
from hangman_words import word_list

lives_remaining = 6  # 14
guessed_letters = ''


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def pick_a_word():
    return random.choice(word_list)  # return word_list[random.randint(0, len(word_list) - 1)]


def get_word_to_display(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word += letter
        else:
            display_word += '_'
    return display_word


def get_guess(word):
    print("Lives remaining 😇: ", str(lives_remaining))  # change this to diagram solution
    print(display_hangman(lives_remaining))
    print(get_word_to_display(word))
    guess = input("Guess a letter or a whole word ⏰: ")
    return guess


def process_guess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)


def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining -= 1
        return False


def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        lives_remaining -= 1
    guessed_letters += guess.lower()
    return all_letters_guessed(word)


def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True


def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        has_won = process_guess(guess, word)
        if has_won:
            print("You win. hurray 👑")
            break
        if lives_remaining == 0:
            print(display_hangman(lives_remaining))
            print("You are hung 🙈", f"The word was {word}")
            break


play()
