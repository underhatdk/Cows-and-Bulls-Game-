import random

number = []
attempts = 0

def MakeNumber():
    for i in range(4):
        x = random.randrange(0,9)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        MakeNumber()
        
def PlayGame():
    global attempts
    attempts += 1
    cows = 0
    bulls = 0
    choice = input("Please enter 4 Digit Number: ")
    guess = []
    for i in range (4):
        guess.append(int(choice[i]))
    for i in range(4):
        for j in range(4):
            if(guess[i] == number[j]):
                cows += 1
    for x in range (4):
        if guess[x] == number[x]:
            bulls += 1
    print("Bulls: ", bulls)
    print("Cows: ", cows)
    if(bulls == 4):
        print("You won after " ,attempts, "attempts!")
    if(bulls != 4):
        PlayGame()

MakeNumber()
PlayGame()
