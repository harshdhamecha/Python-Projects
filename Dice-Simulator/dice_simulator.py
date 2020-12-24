import random as rd
import time

def DiceRoll(attempts):
  '''Main function of Dice Roll'''
  scores = []
  for attempt in range(attempts):
    print('\nAttempts Remaining:', attempts - attempt)
    time.sleep(0.5)
    temp = input('Press enter to roll a dice: ')
    time.sleep(0.7)
    score = rd.randint(1, 6)
    print('You got', score, 'on a dice')
    scores.append(score)
  return scores

def try_more():
  '''Ask the user that whether they want to roll a dice again or not and proceed further accordingly'''
  time.sleep(1)
  decision = input('\nWould you like to roll a dice once again (y/n)? ').lower()
  if decision == 'y':
    time.sleep(0.5)
    temp = input('Press enter to roll a dice: ')
    time.sleep(0.7)
    score = rd.randint(1, 6)
    print('You got', score, 'on a dice')
    scores.append(score)
    try_more()
  elif decision != 'y' and decision != 'n':
    print('You\'ve wrongly pressed key other than \'y\' or \'n\'')
    try_more()
  else:
    return 

def print_scores(scores):
  '''Returns the attempt-wise scores'''
  for score in range(1, len(scores)+1):
    print(f'Attempt {score}: {scores[score-1]}')

# Driver Code
attempts = int(input('How many times would you like to roll a dice? '))
scores = DiceRoll(attempts)

if 6 not in scores:
  time.sleep(0.5)
  print('\nYou haven\'t got the highest number yet!')
  try_more()
else:
  time.sleep(0.5)
  print('\nYou\'ve got 6, Great going buddy!')
  try_more()

print('\nFollowing is your attempt-wise scores:')  
print_scores(scores)
print('\nYou scored total', sum(scores), 'points in', len(scores), 'attempts')
