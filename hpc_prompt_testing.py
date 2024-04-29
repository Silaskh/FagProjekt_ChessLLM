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
    return f"You are playing chess and the board state is {board}. Here you are given a list of legal moves {moves}. You have to chose the best move to make next from the list of legal moves and provide the move exactly as they are given to you. What is your next move given in UCI notation?"
    
def gen_legal_moves(board,frac=1):
    legal_moves = board.legal_moves
    legal_moves = [str(move) for move in legal_moves]
    if frac == 1:
        return legal_moves
    else:
        return np.random.choice(legal_moves, math.floor(frac*len(legal_moves)), replace=False)

def prompt_move_ll2(prompt,board):
    response = ollama.chat(model='llama2:70b', messages=[
            {'role': 'user','content': prompt,},])
    move = response['message']['content']
    for k in range(len(move)):
        if move[k:k+4] in gen_legal_moves(board):
            move = move[k:k+4]
            break
    return move

def prompt_move_ll3(prompt,board):
    response = ollama.chat(model='llama3:70b', messages=[
            {'role': 'user','content': prompt,},])
    move = response['message']['content']
    for k in range(len(move)):
        if move[k:k+4] in gen_legal_moves(board):
            move = move[k:k+4]
            break
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

N = 1000

df = pd.read_csv(r"chessData.csv")

path_to_stockfish = r"C:\Users\Silas Hansen\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe"

amount_legal_ll2 = 0
amount_legal_ll3 = 0

amount_idx_0_ll2 = 0
amount_idx_0_ll3 = 0

amount_optimal_ll2 = 0
amount_optimal_ll3 = 0

##Testing loop##
for i in range(N):
    if i % 100 == 0:
        with open(file_status, "w") as f:
            f.write(f"\n at iteration {i} out of {N}: \n llama2: amount of legal moves {amount_legal_ll2}, amount of idx 0 {amount_idx_0_ll2}, amount of optimal moves {amount_optimal_ll2} \n llama3: amount of legal moves {amount_legal_ll3}, amount of idx 0 {amount_idx_0_ll3}, amount of optimal moves {amount_optimal_ll3} \n")
    fen = df['FEN'][0]
    board = chess.Board(fen)
    legal_moves = gen_legal_moves(board)
    optimal_move = best_move(fen, path_to_stockfish)
    move_ll2 = prompt_move_ll2(gen_prompt2(fen,legal_moves),board)
    move_ll3 = prompt_move_ll3(gen_prompt2(fen,legal_moves),board)
    if move_ll2 in legal_moves:
        amount_legal_ll2 += 1
    if move_ll3 in legal_moves:
        amount_legal_ll3 += 1
    if move_ll2 == legal_moves[0]:
        amount_idx_0_ll2 += 1
    if move_ll3 == legal_moves[0]:
        amount_idx_0_ll3 += 1
    if move_ll2 == optimal_move:
        amount_optimal_ll2 += 1
    if move_ll3 == optimal_move:
        amount_optimal_ll3 += 1

with open(file_data, "w") as f:
    f.write(f"llama2: amount of legal moves {amount_legal_ll2}, amount of idx 0 {amount_idx_0_ll2}, amount of optimal moves {amount_optimal_ll2} \n llama3: amount of legal moves {amount_legal_ll3}, amount of idx 0 {amount_idx_0_ll3}, amount of optimal moves {amount_optimal_ll3} \n")
    
