import random

beat_dict = {"rock": ["lightning", "gun", "air", "water", "dragon", "paper", "devil"],
             "gun": ["lightning", "sponge", "air", "water", "dragon", "paper", "devil"],
             "lightning": ["wolf", "sponge", "air", "water", "dragon", "paper", "devil"],
             "devil": ["wolf", "sponge", "air", "water", "dragon", "paper", "tree"],
             "dragon": ["wolf", "sponge", "air", "water", "human", "paper", "tree"],
             "water": ["wolf", "sponge", "air", "snake", "human", "paper", "tree"],
             "air": ["wolf", "sponge", "scissors", "snake", "human", "paper", "tree"],
             "paper": ["wolf", "sponge", "scissors", "snake", "human", "fire", "tree"],
             "sponge": ["wolf", "rock", "scissors", "snake", "human", "fire", "tree"],
             "wolf": ["gun", "rock", "scissors", "snake", "human", "fire", "tree"],
             "tree": ["gun", "rock", "scissors", "snake", "human", "fire", "lightning"],
             "human": ["gun", "rock", "scissors", "snake", "devil", "fire", "lightning"],
             "snake": ["gun", "rock", "scissors", "dragon", "devil", "fire", "lightning"],
             "scissors": ["gun", "rock", "water", "dragon", "devil", "fire", "lightning"],
             "fire": ["lightning", "gun", "air", "water", "dragon", "rock", "devil"]}
default = ["rock", "paper", "scissors"]
name = input("Enter your name: ")
print(f"Hello, {name}")
type_of_game = input()

if type_of_game == "":
    chosen = default
else:
    a = type_of_game.replace(",", " ")
    chosen = a.split()

with open("rating.txt", "r+") as file:
    for i in file:
        line = i.split()
        if line[0] == name:
            score = int(line[1])
print("Okay, let's start")
while True:
    man = input()
    if man == "!exit":
        print("Bye!")
        break

    if man == "!rating":
        print(score)
        continue
    if man not in chosen:
        print("Invalid input")
        continue
    comp = random.choice(chosen)

    if man == comp:
        print(f"There is a draw ({man})")
        score += 50
        continue

    if man not in beat_dict[comp]:
        print(f"Sorry, but the computer chose {comp}")
        continue

    if man in beat_dict[comp]:
        print(f"Well done. The computer chose {comp} and failed")
        score += 100
        continue


