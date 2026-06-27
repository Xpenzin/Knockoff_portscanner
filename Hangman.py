import random
import time
words = ["Ransomeware", "Spyware", "Worm", "Trojan", "Keylogger"]


#starting print
print("-----------Hangman-----------\n")
print("Choose the number")
print("This game is automatically starting")

time.sleep(1.0)
print("starting game...\n")
time.sleep(0.2)

# words get randomized
ranWord = random.choice(words)
listed_vers_of_words = list(ranWord.lower())
# what users see when word is covered
listed_vers_of_game_words = []
for y in listed_vers_of_words:
    listed_vers_of_game_words += "_"                
        
while True:            
#user attempts to guess the letter of the word
    
    print(listed_vers_of_game_words)
    attempt = input("Try a letter: ").lower()
#game stops after the word is found out
#displays the letter thats in the word and replace the '_' with the appropiate letter if user guess is correct
    if attempt in listed_vers_of_words:
        print(f"The letter '{attempt}' is in the word")
        for value_location, letter in enumerate(listed_vers_of_words):
            if letter == attempt:
                listed_vers_of_game_words[value_location] = attempt
        print(listed_vers_of_game_words)
        
        if listed_vers_of_game_words == listed_vers_of_words:
            print("You have completed the hangman. Congratulations!")
            time.sleep(0.8)
            break
        continue

    elif attempt not in listed_vers_of_words:
        print(f"'{attempt}' is not in the word. Srry")
        continue

