# Guessing Game

import random

num = random.randint(0,50)
tries = 6

print("Welcome to the number guessing game!!!\n")
print("You have 5 Guesses left! The secret number is between 0 and 50, Good Luck!!!!")

while(tries != 0):
           check = int(input("\nEnter a number: "))
           if num == check:
                      print("Well Done!! The answer is {} and you figured it out in ".format(num) + str(6 - tries) + " tries")
                      break
           elif (num-10 < check < num+10):
                      tries-=1
                      print("Oops, not quite! But Warm!! You have {} chances left.".format(tries))
                      
           else:
                      tries-=1
                      print("Oops, not quite! But Cold!! You have {} chances left.".format(tries))
           

if tries == 0:
           print("GAME OVER BRO")

