##IMPORTS##
import chess
import numpy as np
import pandas as pd
import math

df = pd.read_csv('chessData.csv')

def gen_legal_moves(board,frac=1):
    legal_moves = board.legal_moves
    legal_moves = [str(move) for move in legal_moves]
    if frac == 1:
        return legal_moves
    else:
        return np.random.choice(legal_moves, math.floor(frac*len(legal_moves)), replace=False)
##SYNTETIC DATA GENERATION##
def generate_synthetic_data_dict(N,size,seed,df):
    if size == 1:
        return generate_synthetic_data_single(N,seed,df)
    data = []
    np.random.seed(seed)
    for i in range(N):
        dict = {}
        random_list = np.random.multinomial(size, np.ones(size)/size, size=1)[0]
        board = chess.Board(df['FEN'][i])
        legal_moves = gen_legal_moves(board)
        for j in range(size):
            if random_list[j] != 0:
                dict[np.random.choice(legal_moves)] = random_list[j]
        data.append(dict)

    return data

def generate_synthetic_data_single(N,seed,df):
    data = []
    np.random.seed(seed)
    for i in range(N):
        board = chess.Board(df['FEN'][i])
        legal_moves = gen_legal_moves(board)
        data.append(np.random.choice(legal_moves))
    return data

path=("stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe")

