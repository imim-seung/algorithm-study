def check_chess(board):
  w_start='WBWBWBWB'
  b_start='BWBWBWBW'

  start=w_start if board[0][0]=='W' else b_start
  count=0

  for b in board:
    if b[0]=='W':
      

