import random
import string

words = ["python", "java", "swift", "javascript"]
dash = "-"
entered_letters = []
all_entered_letters = []
unraveled_word = ""
won = 0
lost = 0


def wrong_letter():
    if len(letter) > 1 or len(letter) < 1:
        print("Please, input a single letter.")
        return True
    if letter.isupper() or letter not in string.ascii_lowercase:
        print("Please, enter a lowercase letter from the English alphabet.")
        return True
    if letter in all_entered_letters:
        print("You've already guessed this letter.")
        return True
    if letter in entered_letters:
        print("You've already guessed this letter.")
        return True


print(f"H A N G M A N")
while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if choice == "results":
        print(f"You won: {won} times.")
        print(f"You lost: {lost} times.")
        continue
    elif choice == "exit":
        break
    elif choice == "play":
        chosen_word = random.choice(words)
        lives = 8
        while lives > 0:
            print()
            unraveled_word = (''.join(letter if letter in entered_letters else dash for letter in chosen_word))
            if unraveled_word == chosen_word:
                print(f"You guessed the word {chosen_word}!")
                print("You survived!")
                won += 1
                entered_letters.clear()
                all_entered_letters.clear()
                unraveled_word = ""
                break
            print(unraveled_word)
            letter = input("Input a letter: ")
            if wrong_letter():
                continue
            if letter in chosen_word:
                entered_letters.append(letter)
            else:
                print("That letter doesn't appear in the word.")
                all_entered_letters.append(letter)
                lives -= 1
        else:
            print()
            print("You lost!")
            lost += 1
            entered_letters.clear()
            all_entered_letters.clear()
            unraveled_word = ""
    else:
        continue
