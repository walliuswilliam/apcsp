from players import *

class TicTacToe():
  def __init__(self, players, auto=True, starting_player=1):
    self.players = players
    self.set_player_numbers()
    self.starting_player = starting_player

    self.board = '000000000'
    self.winner = None
    self.auto = auto
    
  
  def set_player_numbers(self):
    for i, player in enumerate(self.players):
      player.set_player_number(i+1)

  def update_board(self, index, value):
    board = [i for i in self.board]
    board[index] = str(value)
    self.board = ''.join(board)
  
  def find_open_spaces(self, board):
    return [i for i in range(len(board)) if board[i] == '0']

  def complete_turn(self, player_number):
    player = self.players[player_number-1]
    open_spaces = self.find_open_spaces(self.board)
    chosen_move = player.choose_space(open_spaces, self.board)
    if chosen_move not in open_spaces:
      raise Exception('Invalid Move Chosen')
    self.update_board(chosen_move, player_number)
  
  def check_winner(self):
    board = self.board
    rows = [[board[i+3*j] for i in range(3)] for j in range(3)]
    cols = [[board[j+3*i] for i in range(3)] for j in range(3)]
    diags = [[board[i+3*i] for i in range(3)],[board[i+3*(2-i)] for i in range(3)]]

    for i in (rows + cols + diags):
      if len(set(i)) == 1 and '0' not in i:
        self.winner = int(i[0])

    if self.winner == None:
      if not any('0' in row for row in self.board):
        self.winner = 'Tie'

  def run_to_completion(self):
    while self.winner is None:
      self.complete_turn(self.starting_player)
      self.check_winner()
      if self.winner is not None:
        if not self.auto:
          print(f'\n#1 Victory Royale, Player {self.winner} wins!')
        return self.winner
      if not self.auto:
        self.print_board()

      self.complete_turn(3-self.starting_player)
      self.check_winner()
      if self.winner is not None:
        if not self.auto:
          print(f'\n#1 Victory Royale, Player {self.winner} wins!')
        return self.winner
      if not self.auto:
        self.print_board()
    return self.winner
      
  def print_board(self):
    print("-------")
    board = [[self.board[i+3*j] for i in range(3)] for j in range(3)]
    for row in board:
      for element in row[:-1]:
        print(element, end="  ")
      print(row[-1])
    print("-------")


# game = TicTacToe([RandomPlayer(), RandomPlayer()], auto=False)
# game.run_to_completion()

game = TicTacToe([InputPlayer(), InputPlayer()], auto=False)
game.run_to_completion()
