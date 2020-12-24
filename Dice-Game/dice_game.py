import random as rd
import time

def AllMaximum(scores):
  '''Returns the index of all maximum elements presents in a list'''
  maxi = max(scores)
  return [index for index, item in enumerate(scores) if item == maxi]

def HandleEquals(scores, players, points):
  '''Handles a situation when two or more players scored the same points'''
  if len(set(scores)) == 1:
    print('\nAll the players have scored the same points in this round!')
    for index in range(len(points)):
      points[index] += 1
  else:
    indices = AllMaximum(scores)
    if len(indices) < 2:
      indices = ''.join(str(i) for i in indices)
      print(f'\n{players[int(indices)]} has won in this round!')
      points[int(indices)] += 1
    else:
      print()
      for index in indices:
        points[index] += 1
        print(players[index], end=', ')
      print('--> scored the same points in this round!')

def RoundResult(scores, players, points):
  '''Returns the results of the rounds'''
  if len(scores) != len(set(scores)):
    HandleEquals(scores, players, points)
  else:
    index = scores.index(max(scores))
    points[index] += 1
    print(f'\n{players[index]} has won this round!')

def GameResult(points, players):
  '''Returns the results of the game'''
  if len(set(points)) == 1:
    print(f'\n\nAll the players have scored the same points')
    print('Congatulations! All')
  else:
    indices = AllMaximum(points)
    if len(indices) < 2:
      indices = ''.join(str(i) for i in indices)
      print(f'\n{players[int(indices)]} has won the game!')
      print('Congratulations!', players[int(indices)])
    else:
      print()
      for index in indices:
        print(players[index], end=', ')
      print('--> scored the same points in the game!')

def DiceGame(rounds, n_players, players):
  '''Main function of the Dice Game'''
  points = [0 for _ in range(n_players)]
  for round in range(1, rounds + 1):
    scores = []
    print('\n\nRound:', round)
    for player in players:
      time.sleep(0.4)
      print(f"It's your turn {player}")
      time.sleep(0.2)
      temp = input('Press enter to roll a dice: ')
      score = rd.randint(1, 6)
      time.sleep(0.5)
      print(f'Your score is: {score}')
      scores.append(score)
    RoundResult(scores, players, points)
  GameResult(points, players)
 
def GameRepeat():
  '''Ask the user whether they want to repeat the game or not and proceed further accordingly'''
  time.sleep(0.5)
  decision = input('\n\nWould you like to play the game once again(y/n)? ').lower()
  if decision == 'y':
    main()
  elif decision != 'y' and decision != 'n':
    print('You\'ve wrongly pressed key other than \'y\' or \'n\'')
    GameRepeat()
  else:
    return

# Driver Code
def main():
  '''Main function'''
  rounds = int(input('\nEnter the total number of rounds you want to play for: '))
  n_players = int(input('Enter the total number of players: '))
  players = []

  for player in range(1, n_players+1):
    players.append(input(f'Enter the name of player{player}: '))

  DiceGame(rounds, n_players, players)
  GameRepeat()

print('-------------Dice Game---------------')
main()
