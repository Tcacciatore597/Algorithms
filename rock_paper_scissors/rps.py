#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  oops = [[]]
  choices = [['rock'], ['paper'], ['schissors']]
  if n < 1:
    return oops
  elif n == 1:
    return choices
  # loop through choices and add choices to each element
  else:
    for x in choices:
      #do the adding and concatenation of sub arrays

      while n > 0:
        rock_paper_scissors(n)
        n -= 1
        
  return choices

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

rock_paper_scissors(2)