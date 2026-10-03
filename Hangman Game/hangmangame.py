import random 

words=['instagram',"facebook","enjoy","hungry"]

word=random.choice(words)
guessed=[]

attempts=6

print("Welcome to Hangman!")

while attempts>0:
    display=""
    for letter in word:
        if letter in guessed:
            display+=letter+""
        else:
            display+="_"
            
    print("\n Word:",display)
    print("Incorrect attempts left:",attempts)
    
    if all(letter in guessed for letter in word):
        print("Congratulations! you guessed the word:",word)
        break
    
    guess=input("Guess a letter:").lower()
    
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue
    
    guessed.append(guess)
    
    if guess in word:
        print("Correct guess!")
    else:
        attempts-=1
        print("Wrong guess!")
        
    if attempts==0:
        print("\n You lost! The word was:",word)