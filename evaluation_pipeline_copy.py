##IMPORTS##
import chess
import numpy as np
import pandas as pd
import math
import chess.engine

df = pd.read_csv('chessData.csv')

def gen_legal_moves(board,frac=1):
    legal_moves = board.legal_moves
    legal_moves = [str(move) for move in legal_moves]
    if frac == 1:
        return legal_moves
    else:
        return np.random.choice(legal_moves, math.floor(frac*len(legal_moves)), replace=False)
##SYNTETIC DATA GENERATION##
def generate_synthetic_data_dict(N,size,df,seed=1):
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

path=(r"stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe")

def evaluate_move(board, move, path):
    #Evaluates the move before move and after move return the difference
    board1 = board.copy()
    board1.push(chess.Move.from_uci(move))
    board2 = board.copy()
    #Return differnce of board1 and board2


def amount_legal_moves_taken(l , df):
    amount = 0
    for i in range(len(l)):
        board = chess.Board(df['FEN'][i])
        legal_moves = gen_legal_moves(board)
        if l[i] in legal_moves:
            amount += 1
    return amount

def amount_index_zero(l,df):
    amount = 0
    for i in range(len(l)):
        board = chess.Board(df['FEN'][i])
        legal_moves = gen_legal_moves(board)
        if l[i] == legal_moves[0]:
            amount += 1
    return amount

def evaluate_moves(fen, move_uci, dataframe):
     # Path to Stockfish executable
    stockfish_path = r"stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe"
    
    # Load Stockfish engine
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        engine.configure({"Threads": 1})  # Configure Stockfish to run in single-threaded mode for consistency
        
        # Create a chess board from FEN
        board = chess.Board(fen)
        
        # Determine which player is to move
        is_white_to_move = board.turn == chess.WHITE
        
        # Evaluate the initial position
        initial_info = engine.analyse(board, chess.engine.Limit(time=1.0))  # Increased time limit for stability
        initial_score = initial_info["score"].white().score(mate_score=10000)  # Get the POV score for White
        
        # If it's Black to move, invert the score
        if not is_white_to_move:
            initial_score = -initial_score
        
        # Generate all legal moves
        legal_moves = list(board.legal_moves)

        board = chess.Board(fen)
        board.push(chess.Move.from_uci(move_uci))
        info = engine.analyse(board, chess.engine.Limit(time=0.1))  # Increased time limit for stability
        move_score_uci = info["score"].white().score(mate_score=10000)  # Get the POV score for White
        # If it's Black to move, invert the score
        if not is_white_to_move:
            move_score_uci = -move_score_uci
        move_uci_difference = move_score_uci - initial_score
        
        # Evaluate all legal moves
        move_differences = []
        for move in legal_moves:
            board = chess.Board(fen)
            board.push(move)
            info = engine.analyse(board, chess.engine.Limit(time=0.1))  # Increased time limit for stability
            move_score = info["score"].white().score(mate_score=10000)  # Get the POV score for White
            # If it's Black to move, invert the score
            if not is_white_to_move:
                move_score = -move_score
            difference = move_score - initial_score
            move_differences.append((move.uci(), difference))
            board.pop()
        
        # Convert to DataFrame
        moves_df = pd.DataFrame(move_differences, columns=['move', 'score_difference'])
        moves_df.head()

       
        return move_uci_difference,initial_score, moves_df
        

def percentiles(moves_df):
        score_75th_percentile = np.percentile(moves_df['score_difference'], 75)
        score_25th_percentile = np.percentile(moves_df['score_difference'], 25)
        score_50th_percentile = np.percentile(moves_df['score_difference'], 50)
        # Return results
        result = {
            "score_75th_percentile": score_75th_percentile,
            "score_50th_percentile": score_50th_percentile,
            "score_25th_percentile": score_25th_percentile,}
        return result

def in_percentile(score,percentile):
    if score >= percentile["score_75th_percentile"]:
        return np.array([0,0,0,1])
    elif percentile["score_50th_percentile"] <= score < percentile["score_75th_percentile"]:
        return np.array([0,0,1,0])
    elif percentile["score_25th_percentile"] <= score < percentile["score_50th_percentile"]:
        return np.array([0,1,0,0])
    else:
        return np.array([1,0,0,0])
    
def percentile_distribution(moves,df):
    result = np.zeros(4)
    for i in range(len(moves)):
        move_difference, inital_score, moves_df = evaluate_moves(df['FEN'][i], moves[i], df)
        result += in_percentile(move_difference,percentiles(moves_df))
    return result

def stockfish_score_function(data, df):
    stockfish_score = []
    for i in range(len(data)):
        move = data[i]
        fen = df['FEN'][i]
        move_uci_difference, initial_score, moves_df = evaluate_moves(fen, move, "hej")
        stockfish_score.append(max(moves_df['score_difference']))
    return stockfish_score

def dict_to_move(dict):
    #chose the key with the highest value
    move = max(dict, key=dict.get)
    return move

def ensemble_score(dicts, df):
    #takes a list of dictionaries and returns the average score of the moves
    ensemble_scores = []
    for i in range(len(dicts)):
        fen = df['FEN'][i]
        move = dict_to_move(dicts[i])
        move_uci_difference, initial_score, moves_df = evaluate_moves(fen, move, "hej")
        ensemble_scores.append(move_uci_difference)
    return ensemble_scores
      
# Baseline / Random Model
                          
def random_model(df, data):
    random_moves = []
    for i in range(len(data)):
        Fen = df['FEN'][i]
        board = chess.Board(Fen)
        legal_moves = gen_legal_moves(board,frac=1)
        random_moves.append(np.random.choice(legal_moves))
    return random_moves

def percentage(data):
    N = len(data)
    n = 0
    with open(data) as f:
        for line in f:
            inx, move = line.split(":")
            if move is not None:
                n += 1
    return n/N

def p_list(list):
    p = [0]
    for i in range(len(list)):
        p.append(percentage(list[i]))
    return p