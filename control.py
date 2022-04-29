#Move(board, letter, move): board[move] = letter
# def isWinner(bo, le): #Учитываязаполнениеигровогополяибуквыигрока,этафункциявозвращаетTrue,еслиигроквыиграл.
# # Мы используем "bo" вместо "board" и "le" вместо "letter", поэтому нам не нужно много печатать. return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
# (bo[4] == le and bo[5] == le and bo[6] == le) or # через центр
# (bo[1] == le and bo[2] == le and bo[3] == le) or # через низ
# (bo[7] == le and bo[4] == le and bo[1] == le) or # вниз по левой стороне (bo[8] == le and bo[5] == le and bo[2] == le) or # вниз по центру
# (bo[9] == le and bo[6] == le and bo[3] == le) or # вниз по правой стороне (bo[7] == le and bo[5] == le and bo[3] == le) or # по диагонали
# (bo[9] == le and bo[5] == le and bo[1] == le)) # по диагонали
# getBoardCopy(board):

def move_step(symbol):
    while True:
        value = input('куда поставить?: '+symbol+" ?")
        if not (value in '123456789'):
            print('ошибочный ввод, повторите')
            continue
        value = int(value)
        if str(board[value -1]) in 'xo':
            print('эта клетка уже занята')
            continue
        board[value - 1] = symbol
        break

