import random

colours = ['red','blue','green','yellow','black','brown','white','pink']

while True: 
    guess = input("Guess a colour: ")
    random_colour = colours[random.randint(0,len(colours)-1)]

    while True:
        if guess.lower() == random_colour:
            break
        else :
            guess = input("Nope! Guess a colour again: ")
    print ("You guessed it ",guess)
    ans = input("Let's play again ? Type 'no' to quit")
    if ans.lower() == 'no':
        break
print("Thanks for playing")
    
