#Step 5

import random
import hangman_art
import hangman_words 



print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
End_Of_The_Game=False
lives=6

#If you want to check the chosen word:
#print(f'Pssst, the solution is {chosen_word}.') 

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while End_Of_The_Game is False:
  guess = input("Guess a letter: ").lower()
  if guess not in chosen_word:
    lives-=1
    print(f"you guessed a latter {guess}, that's not in the word. you lose a life")
    print(hangman_art.stages[lives])
    if lives == 0:
      print("The game is over")
      End_Of_The_Game=True

  
  elif guess in display:
    print(hangman_art.stages[lives])
    print(f"you've already guessed {guess}")
    
  else:
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
          print(hangman_art.stages[lives])
          display[position] = letter
          
          if "_" not in display:
            print("Great!!! You are won!")
            End_Of_The_Game=True
    
    
      
            
  print(display)