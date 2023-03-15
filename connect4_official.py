"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
Authors: David Le, Randil Hettiarachchi, Rathan Murugesan Senthil, 
Last updated: 13/03/2023
"""
import random
import os

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


def validate_input(prompt, valid_inputs):

	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""

	# Implement your solution below
	input_option = input(prompt)

	# Loops until it the input is valid
	while input_option not in valid_inputs:
		print("Invalid input, please try again.")
		input_option = input(prompt)
	return input_option


def create_board():

	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	# Implement your solution below
	board = [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0]
	]
	
	return board


def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	# Implement your solution below
	print("========== Connect4 =========")
	print("Player 1: X       Player 2: O")
	print("")
	print("  1   2   3   4   5   6   7")

	for row in range(6):
		print(" --- --- --- --- --- --- ---")
		for column in range(7): # MIMGHT NEED TO REFERENCE
			if board[row][column] == 0:
				print("|   ",end="")
			elif board[row][column] == 1:
				print("| X ",end="")
			else: # when the the element is 2
				print("| O ",end="")
		print("|")
	print(" --- --- --- --- --- --- ---")
	print("=============================")


def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player who is dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	# Implement your solution below
	if board[0][column - 1] == 0:
		for row in range(5, -1, -1):
			if board[row][column - 1] == 0:
				board[row][column - 1] = player
				break
		return True
	else:
		return False


def execute_player_turn(player, board):
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	column = int(validate_input("Player " + str(player) + ", please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5", "6", "7"]))
	
	while drop_piece(board, player, column) == False:
		print("That column is full, please try again.")
		column = int(validate_input("Player " + str(player) + ", please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5", "6", "7"]))
	if drop_piece(board, player, column):
		return column


def end_of_game(board): # Question 6
	"""
	Checks if the game has ended with a winner
	or a draw.

	The check will happen from bottom left, left to right 

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""
	# Implement your solution below
	for row in range(len(board)-1, -1, -1):
		for column in range(len(board[row])):
			if (board[row][column] == 0):
				continue #skip this square
			horizontal_winner, vertical_winner, diagonal_winner = horizontal_check(board, row, column), vertical_check(board, row, column), diagonal_check(board, row, column)
			if (horizontal_winner != 0):
				return horizontal_winner
			if(vertical_winner != 0):
				return vertical_winner
			if(diagonal_winner != 0 ):
				return diagonal_winner
		
	for column in range(len(board[0])):
		if(board[0][column] == 0):
			return 0
	return 3

'''The 0 in the code below do not represent its not game over but rather that there is not a win from that position '''

#Occurs left to right. No need to go other way as this would check the same thing
def horizontal_check(board, row, column):
	checking = board[row][column] #Which player is being checked
	if (column + 3 >= 7):
		return 0 #As you can't get a horizontal win from this point
	for column_check in range(1, 4):
		if(board[row][column+column_check] != checking):
			return 0		
	return checking

#No need to check downwards as check vertically would have been done from the lower piece 
def vertical_check(board, row, column):
	checking = board[row][column] #Which player is being checked
	if (row - 3 < 0):
		return 0 #As you can't get a vertical win from this point
	for row_check in range(1, 4):
		if(board[row-row_check][column] != checking):
			return 0		
	return checking

#Both diagonals need to be checked
def diagonal_check(board, row, column):
	checking = board[row][column] 
	winning = False

	#left diagonal check 
	if (row - 3 >= 0 and column - 3 >= 0):
		for i in range(1, 4):
			if (board[row - i][column-i] == checking):
				winning = True
			if (board[row - i][column-i] != checking):
				winning = False
				break
		if (winning):
			return checking

	#right diagonal check
	if (row - 3 >= 0 and column + 3 < 7):
		for i in range(1, 4):
			if (board[row - i][column+i] == checking):
				winning = True
			else:
				winning = False
				break
		if (winning):
			return checking
	return 0
		
def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	raise NotImplementedError


def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty. 
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	raise NotImplementedError


def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.
	<Insert player strategy here>

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


if __name__ == "__main__":
	main()

print ('Hello world')


