#!/usr/bin/python3

class Board:

	def __init__(self):
		self.build()

	def build(self)->'str':
		rows, cols = (3, 3) 
		arr = [[0 for i in range(cols)] for j in range(rows)] 
		self.board = arr

	def printb(self):
		arr = self.board
		print('   |   |')
		print(' ' + str(arr[0][0]) + ' | ' + str(arr[1][0]) + ' | ' + str(arr[2][0]))
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + str(arr[0][1]) + ' | ' + str(arr[1][1]) + ' | ' + str(arr[2][1]))
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + str(arr[0][2]) + ' | ' + str(arr[1][2]) + ' | ' + str(arr[2][2]))
		print('   |   |')

	def move(self, col, row, pl)->'pos':
		if self.board[col][row] == 0:
			self.board[col][row] = pl.color
			return 0
		else:
			print('There exists a character in the position you chose')
			return 1

	def check(self)->'int':
		x_condition = ['X', 'X', 'X']
		o_condition = ['O', 'O', 'O']
		h_check = self.board.copy()
		v_check = [[]]
		d_check = [[]]
		tempv0 = []
		tempv1 = []
		tempv2 = []
		tempd0 = []
		tempd1 = []
		for i in self.board:
			tempv0.append(i[0])
			tempv1.append(i[1])
			tempv2.append(i[2])
			if self.board.index(i) == 0:
				tempd0.append(i[0])
				tempd1.append(i[2])
			if self.board.index(i) == 1:
				tempd0.append(i[1])
				tempd1.append(i[1])
			if self.board.index(i) == 2:
				tempd0.append(i[2])
				tempd1.append(i[0])
		v_check.append(tempv0)
		v_check.append(tempv1)
		v_check.append(tempv2)
		d_check.append(tempd0)
		d_check.append(tempd1)

		for h in h_check:
			if h == x_condition:
				return 1
			if h == o_condition:
				return 2
		for v in v_check:
			if v == x_condition:
				return 1
			if v == o_condition:
				return 2
		for d in d_check:
			if d == x_condition:
				return 1
			if d == o_condition:
				return 2
		return 0






