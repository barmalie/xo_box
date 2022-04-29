'''def inputPlayerLetter():
# Разрешение игроку ввести букву, которую он выбирает.
# Возвращает список, в котором буква игрока — первый элемент, а буква компьютера — второй.

	letter = ''
	while not (letter == 'Х' or letter == 'О'):
			print('Вы выбираете Х или О?')
			letter = input().upper()
print(inputPlayerLetter())'''


# def inputPlayerLetter():
#     # Разрешение игроку ввести букву, которую он выбирает.
#     # Возвращает список, в котором буква игрока — первый элемент, а буква компьютера — второй.
#
#     letter = ''
#     while not (letter == 'Х' or letter == 'О'):
#         print('Вы выбираете Х или О?')
#     letter = input().upper()
# Первым элементом списка является буква игрока, вторым — буква компьютера.
# if letter == 'Х':
#     return ['Х', 'О']

# else:
#     return ['О', 'Х']

def winner():
    for _ in wins_coord:
        if (board[_[0] - 1]) == (board[_[1] - 1]) == (board[_[2] - 1]):
            return board[_[1] - 1]
        else:
            return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 5:
            winner = check_win()
            if winner:
                draw_board()
            print((winner, "выиграл")
            break
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья")
            break

