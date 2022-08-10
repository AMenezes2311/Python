#Created by Andre Menezes
from random import randint
from time import sleep
def get_user_guess(guess):
  guess = raw_input("Guess a number: ")
  return guess

def roll_dice(number_of_sides):
  first_row = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * number_of_sides
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "You should put a number between 2 and 36"
  else:
      print "Rolling..."
      sleep(2)
      print "The 1st roll is: %d" % fisrt_roll
      sleep(1)
      print "The 2nd roll is: %d" % second_roll
      sleep(1)
      total_roll = first_roll + second_roll
      print total_roll
      print "Result..."
      sleep(1)
      if guess == total_row:
        print "You won"
      else:
        print "You lost, try again"
