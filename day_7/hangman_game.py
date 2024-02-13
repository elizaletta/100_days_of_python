#Step 1 
import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.') 

#Create blanks
display = []
for each_letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")

#TODO2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
while not end_of_game:
    guess = (input('Guess a letter: ')).lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("You've already guessed this letter.")
        print(f"{' '.join(display)}")

    for position in range(word_length): #Loop through each position in the chosen_word; If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

#TODO2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."
#Join all the elements in the list and turn it into a String.
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life.") #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")            
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])
