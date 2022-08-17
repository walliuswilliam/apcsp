import random

class RandomPlayer:
  def __init__(self):
    self.player_number = None
    self.board = None

  def set_player_number(self, n):
    self.player_number = n
  
  def choose_space(self, possible_moves, board):
    return possible_moves[random.randrange(len(possible_moves))]

class InputPlayer:
  def __init__(self):
    self.player_number = None
    self.board = None

  def set_player_number(self, n):
    self.player_number = n
  
  def choose_space(self, possible_moves, board):
    possible_moves = [str(i+1) for i in possible_moves]
    while True:
      move = input(f'Player {self.player_number}, Choose a Move (type "help" for help or "moves" for possible moves)\n')
      if move == 'help':
        print('Choose a number:\n-------\n1  2  3\n4  5  6\n7  8  9\n-------')
      elif move == 'moves':
        print(f'Possible moves: {possible_moves}')
      elif move in possible_moves:
        break
      else:
        print('Invalid move')        
    return int(move)-1
