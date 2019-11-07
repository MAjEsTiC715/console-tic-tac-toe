from Board import Board
from Player import Player

def main():

	board = Board()
	player1 = Player('X')
	player2 = Player('O')
	winner = False

	while winner == False:
		if Player.turn % 2 == 0:
			col = int(input('It is your turn: '+ player1.color +' choose col: '))
			row = int(input('It is your turn: '+ player1.color +' choose row: '))
			board.move(col, row, player1)
			board.printb()
			Player.turn += 1
		else:
			col = int(input('It is your turn: '+ player2.color +' choose col: '))
			row = int(input('It is your turn: '+ player2.color +' choose row: '))
			m = board.move(col, row, player2)
			board.printb()
			if m == 0:
				Player.turn += 1
		c = board.check()
		if c == 1:
			winner = True
			print('X wins')
		if c == 2:
			winner = True
			print('O wins')

if __name__ == '__main__':
	main()