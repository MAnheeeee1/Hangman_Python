import random
import hangman_art
import hangman_word

chosen_word = list(random.choice(hangman_word.word_list))
display = ["_"] * len(chosen_word)
correct_or_not = False
game_over = False
lifes = 7
print(hangman_art.logo)
while game_over != True:
    correct_or_not = False
    print(f'Pssst, the solution is {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    current_index = 0
    for letters in chosen_word:
        if letters == guess:
            display[current_index] = guess
            correct_or_not = True
        current_index += 1
    print(display)
    if correct_or_not == True:
        print("You guessed correct!")
    else:
        lifes -= 1
        print(hangman_art.stages[lifes])
        print("You guessed wrong")
        print(f"Life left: {lifes}")
    if lifes == 0:
        print("You lost all lives!\nYou have lost the game!")
        game_over = True
    elif display == chosen_word:
        print("You have won the game!")
        game_over = True




