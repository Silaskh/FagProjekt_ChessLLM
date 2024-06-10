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


def amount_75th_percentile():
    pass

def amount_25th_percentile():
    pass

def amount_mean_taken_over_mu_moves():
    pass


amount = amount_index_zero(generate_synthetic_data_dict(10,1,df,1),df)
amount 

def evaluate_moves(fen, move_uci, dataframe):
    # Path to Stockfish executable
    stockfish_path = "stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe"
    
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
        
        # Evaluate all legal moves
        move_differences = []
        for move in legal_moves:
            board.push(move)
            info = engine.analyse(board, chess.engine.Limit(time=1.0))  # Increased time limit for stability
            move_score = info["score"].white().score(mate_score=10000)  # Get the POV score for White
            # If it's Black to move, invert the score
            if not is_white_to_move:
                move_score = -move_score
            difference = move_score - initial_score
            move_differences.append((move.uci(), difference))
            board.pop()
        
        # Convert to DataFrame
        moves_df = pd.DataFrame(move_differences, columns=['move', 'score_difference'])
        
        # Calculate the 75th percentile score difference
        score_75th_percentile = np.percentile(moves_df['score_difference'], 75)
        score_25th_percentile = np.percentile(moves_df['score_difference'], 25)
        score_50th_percentile = np.percentile(moves_df['score_difference'], 50)
    
        
        # Get the score difference of the provided move
        provided_move_score_difference = moves_df.loc[moves_df['move'] == move_uci, 'score_difference'].values[0]
        
        # Check if the provided move is within the 75th percentile
        is_within_75th_percentile = provided_move_score_difference >= score_75th_percentile
        is_within_50th_percentile = provided_move_score_difference >= score_50th_percentile
        is_within_25th_percentile = provided_move_score_difference >= score_25th_percentile
        
        # Return results
        result = {
            "provided_move": move_uci,
            "provided_move_score_difference": provided_move_score_difference,
            "score_75th_percentile": score_75th_percentile,
            "score_50th_percentile": score_50th_percentile,
            "score_25th_percentile": score_25th_percentile,
            "is_within_75th_percentile": is_within_75th_percentile,
            "is_within_50th_percentile": is_within_50th_percentile,
            "is_within_25th_percentile": is_within_25th_percentile
        }
        
        return result

# Example usage:
fen = df['FEN'][0]
move_uci = generate_synthetic_data_dict(1, 1, df,100)[0]
print(move_uci)
dataframe = df  # Replace with your actual dataframe if needed

result = evaluate_moves(fen, move_uci, dataframe)
print(result)
