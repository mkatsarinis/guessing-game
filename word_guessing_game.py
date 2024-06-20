import random

def word_guessing_game():
    print("welcome to the word guessing game!")
    words=('python', 'programming', 'computer', 'code', 'challenge', 'learning')
    #generate a random word from the list
    secret_word=random.choice(words)
    
    guessed_letters = set ()
    attempts=0
    max_attempts = 10
    
    while True:
        display_word= "".join(letter if letter in guessed_letters else '_' for letter in secret_word)
        print(f"current word: {display_word}")
        
        guess = input("guess a letter:").lower()
        attempts +=1
        
        if guess in guessed_letters:
            print('you already guessed that letter. try again')
            continue
        
        guessed_letters.add(guess)
        
        if all(letter in guessed_letters for letter in secret_word):
            print(f"congratulation! you gueseed the word '{secret_word}' in {attempts} attempts." )
            break
        else:
            print("incorrext guess. try again")
        if attempts == max_attempts:
            print(f"sorry, you've reached the maximum attemopts")
            break
if __name__=="__main__":
    word_guessing_game()