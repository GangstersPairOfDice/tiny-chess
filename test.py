import chess.pgn

pgn = open("test.pgn")

game = chess.pgn.read_game(pgn)

# iter through all moves and play them on a board.

board = game.board()

print(board)
print('')

for move in game.mainline_moves():
  board.push(move)
  print(board)
  print('')

board
print(board.is_checkmate())
