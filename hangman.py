def hangman():
  Continue=True
  while Continue:
      secret_word=input("Input secret word : ").upper()
      blanks = "_" * len(secret_word)
      guesses_left = 5
      failedGuesses=0
      
      while guesses_left > -1 and not blanks == secret_word:
        print("Your Progress : ",blanks)
        print ("Chances Left : ",str(guesses_left))
        
        guess = input("Guess :").upper()
        
        if len(guess) != 1:
          print ("Warning : You must guess exactly one character!")
          
        elif guess in secret_word:
          print ("Good!!! That letter is in the secret word!")
          blanks = total_blanks(secret_word, blanks, guess)
          
        else:
          print ("Wrong Guess!!!")
          guesses_left -= 1
          failedGuesses+=1
          if failedGuesses == 1:
                print("YOUR STATUS : O")
          elif failedGuesses == 2:
                print("YOUR STATUS : O-")
          elif failedGuesses == 3:
                print("YOUR STATUS : O_/")
          elif failedGuesses == 4:
                print("YOUR STATUS : O-<")
          elif failedGuesses == 5:
                print("YOUR STATUS : O+<")
          elif failedGuesses == 6:
                print("YOU DIED !!!\n")
        
      if guesses_left < 0:
        print ("You lose! The word was: " + str(secret_word),"\nBetter luck next Time !")
      else:
        print ("Congrats! You win. The word was: " + str(secret_word))
      quit = input("Do you want to quit? (Yes/No): ").upper()
      if quit == "YES" or quit == "Y" or quit=='y':
          Continue = False
  print()
  print("Thank you for playing Hangman!\nHave A Nice Day!")
        

def total_blanks(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     
      
    else:
      result = result + cur_dash[i]
      
  return result
    
hangman()
