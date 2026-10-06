'''
Write a program that generates a random number and asks the user to guess it.

If the user's guess is higher than the actual number,
display "Lower number please".

If the user's guess is lower than the actual number,
display "Higher number please".

When the user guesses the correct number,
display the number of guesses the player used to find it.

Hint: Use the random module.
'''

import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    
    a = int(input("Guess the number : "))
    if(a > n):
        print("Lower number please!")
        guesses += 1
    else:
        print("Higher number please!")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")