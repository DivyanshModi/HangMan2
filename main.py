import random
import hangman_art   #for logo and basic graphics

import hangman_words #for list of words
#word_list = ["ardvark", "baboon", "camel"]
print(hangman_art.logo)
word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



#Testing code
#print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print("Already guessed , Use another word",guess)
  else:

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")   #to print as a _ _ h a (alpha)


    if "_" not in display:
        end_of_game = True
        print("You win.")


  print(hangman_art.stages[lives])