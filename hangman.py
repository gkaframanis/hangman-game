import random
import hangman_words
import hangman_art

stages = hangman_art.stages

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
lives = 6

print(f"{hangman_art.logo}\n")

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print("\n")

    if guess in display:
        print(f"You've already guessed {guess}\n")

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life.\n")
    else:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
            

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")
        
    if "_" not in display:
        end_of_game = True
        print("You win!!!")

    if lives == 0:
        end_of_game = True
        print("You lose.")

    print(stages[lives])
