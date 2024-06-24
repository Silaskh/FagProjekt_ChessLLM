# Importing all relevant and necessary modules
import numpy as np 
import pandas as pd 
import os
import chess
import math
import matplotlib.pyplot as plt
import ollama
from stockfish import Stockfish

def gen_prompt2(board,moves, n=10):
	msg = "You are apart of en ensemble of langauge models.You are playing chess and the board state is " + str(board) + "Here you are given a list of legal moves" + str(moves) + "You have to vote on the best move to make next from the list of legal moves and provide the move exactly as they are given to you. What is your next move given in UCI notation?"
	return msg
    
def gen_legal_moves(board,frac=1):
	legal_moves = board.legal_moves
	legal_moves = [str(move) for move in legal_moves]
	if frac == 1:
		return legal_moves
	else:
		return np.random.choice(legal_moves, math.floor(frac*len(legal_moves)), replace=False)

def prompt_move_ll3(prompt,board):
	response = ollama.chat(model='llama3:70b', messages=[{'role': 'user','content': prompt,},])
	move = response['message']['content']
	for k in range(len(move)):
		if move[k:k+4] in gen_legal_moves(board):
			move = move[k:k+4]
			break
	if move not in gen_legal_moves(board):
		move = " "
	return move


def evaluate_move_stockfish(fen,move,path_to_stockfish):
	board = chess.Board(fen)
	stockfish = Stockfish(path_to_stockfish)
	board.push_uci(move)
	return stockfish.get_evaluation()["value"]

def best_move(fen, path_to_stockfish):
	board = chess.Board(fen)
	legal_moves = gen_legal_moves(board)
	best_move = legal_moves[0]
	best_move_eval = evaluate_move_stockfish(fen, best_move, path_to_stockfish)
	for move in legal_moves:
		move_eval = evaluate_move_stockfish(fen, move, path_to_stockfish)
		if move_eval > best_move_eval:
			best_move = move
			best_move_eval = move_eval
	return best_move

###Code below ##

#Initialising the variables
file_status = "status.txt"
file_data = "data.txt"
file_moves = "moves.txt"

N = 10**6

df = pd.read_csv(r"shuffled.csv")

path_to_stockfish = r"stockfish\stockfish-windows-x86-64-avx2.exe"

amount_legal_ll2 = 0
amount_legal_ll3 = 0

amount_idx_0_ll2 = 0
amount_idx_0_ll3 = 0

amount_optimal_ll2 = 0
amount_optimal_ll3 = 0

##Testing loop##
for i in range(32, N):
	string = str(i) +": "
	fen = df['FEN'][i]
	board = chess.Board(fen)
	legal_moves = gen_legal_moves(board)
	for j in range(20):
		move_ll3 = prompt_move_ll3(gen_prompt2(fen,legal_moves),board)
		if j != 19:
			string = string + move_ll3 + ","
		else: 
			string = string + move_ll3  
	with open(file_moves, "a") as f:
		f.write(string + "\n" )
