##IMPORTS##
import chess
import numpy as np
import pandas as pd
import math
import chess.engine
import pickle as pkl

df = pd.read_csv('chessData.csv')

def gen_legal_moves(board,frac=1):
    legal_moves = board.legal_moves
    legal_moves = [str(move) for move in legal_moves]
    if frac == 1:
        return legal_moves
    else:
        return np.random.choice(legal_moves, math.floor(frac*len(legal_moves)), replace=False)
    
def check_legal_moves(data, df):
    for i in range(len(data)):
        board = chess.Board(df['FEN'][i])
        legal_moves = gen_legal_moves(board)
        if data[i] not in legal_moves:
            print(i)
    
##SYNTETIC DATA GENERATION - Random model ##
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

def evaluate_moves(fen, move, elo=1350):
    stockfish_path = r"stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe"
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        engine.configure({"Threads": 8,"UCI_LimitStrength": True, "UCI_Elo": elo})  # Increased number of threads for stability
        # Create a chess board from FEN
        board = chess.Board(fen)
        # Determine which player is to move
        is_white_to_move = board.turn == chess.WHITE
        
        board = chess.Board(fen)
        board.push(chess.Move.from_uci(move))
        info = engine.analyse(board, chess.engine.Limit(time=0.1))  # Increased time limit for stability
        move_score= info["score"].white().score(mate_score=10000)  # Get the POV score for White
        # If it's Black to move, invert the score
        if not is_white_to_move:
            move_score = -move_score
        # engine.quit()  # Quit the engine after use
    return move_score

def moves_dataframe(fen, elo=1350):   
    legal_moves = gen_legal_moves(chess.Board(fen))
        
    # Evaluate all legal moves
    move_score = []
    for move in legal_moves:
        score = evaluate_moves(fen, move, elo=elo)
        move_score.append((move, score))
        
    
    # Convert to DataFrame
    moves_df = pd.DataFrame(move_score, columns=['move', 'move_score'])   
    return moves_df


def move_difference(data, df, filename, elo=1350):
    score_difference = []
    moves_df_list = []
    move_scores = []
    for i in range(len(data)):
        if data[i] == "None":
            continue
        moves_df = moves_dataframe(df['FEN'][i], elo=elo)
        moves_df_list.append(moves_df)
        move_score = moves_df['move_score'][moves_df['move'] == data[i]].values[0]
        move_scores.append(move_score)
        print(i)
        stockfish_score = max(moves_df['move_score'])
        score_difference.append(stockfish_score-move_score)
    
    with open(filename, 'wb') as file:
        pkl.dump({
            'score_difference': score_difference,
            'moves_df_list': moves_df_list,
            'move_scores': move_scores
        }, file)
        
    return move_scores, moves_df_list, score_difference
        

def percentiles(moves_df):
        score_75th_percentile = np.percentile(moves_df['move_score'], 75)
        score_25th_percentile = np.percentile(moves_df['move_score'], 25)
        score_50th_percentile = np.percentile(moves_df['move_score'], 50)
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
    
def percentile_distribution(moves, df, filename1, filename2, elo=1350):
    result = np.zeros(4)
    move_scores, moves_df_list, score_difference = move_difference(moves, df, filename1, elo=elo)
    
    # Open the file in append mode
    with open(filename2, 'a') as file:
        for i in range(len(score_difference)):
            if moves[i] == "None":
                continue
            percentile = percentiles(moves_df_list[i])
            result += in_percentile(move_scores[i], percentile)
            
            # Convert the numpy array to a string
            result_str = np.array2string(result)
            
            # Write the string to the text file
            file.write(f"{i}: {result_str}\n")
            
    return result

#### HOW TO OPEN THE FILE ####
# with open('counts_random_1350.txt', 'r') as file:
#     counts_random_1350_str = file.read()

# # Convert the string back to a numpy array
# counts_random_1350 = np.fromstring(counts_random_1350_str.strip('[]'), sep=' ')

# def stockfish_score_function(N, df,elo=1350):
#     stockfish_score = []
#     for i in range(N):
#         moves_df = moves_dataframe(df['FEN'][i],elo=elo)
#         stockfish_score.append(max(moves_df['move_score']))
#     return stockfish_score

# def dict_to_move(dict):
#     #chose the key with the highest value
#     move = max(dict, key=dict.get)
#     return move

# def score(data, df, elo=1350):
#     #takes a list of dictionaries and returns the average score of the moves
#     scores = []
#     for i in range(len(data)):
#         fen = df['FEN'][i]
#         move = data[i]
#         if move != None:
#             relative_move_difference = evaluate_move(fen, move, elo=elo)
#             scores.append(relative_move_difference)
#     return scores
      
# Baseline / Random Model
                          
# def random_model(df, data):
#     random_moves = []
#     for i in range(len(data)):
#         Fen = df['FEN'][i]
#         board = chess.Board(Fen)
#         legal_moves = gen_legal_moves(board,frac=1)
#         random_moves.append(np.random.choice(legal_moves))
#     return random_moves

def percentage(data):
    N = 101
    n = 0
    with open(data) as f:
        for line in f:
            inx, move = line.split(":")
            if move != " None\n":
                n += 1
    return n/N

def p_list(list):
    p = [0]
    for i in range(len(list)):
        p.append(percentage(list[i]))
    return p

def get_moves(data):
    moves = []
    with open(data) as f:
        for line in f:
            inx, move = line.split(":")
            move = move[1:-1]
            moves.append(move)
    return moves

def get_ensemble_output_dict():
    moves = []
    with open("ensemble_output.txt", "r") as file:
        for line in file:
            #Remove the everything before the first : and the space after
            line = line[line.find(':')+1:]
            #Remove the newline character
            line = line[:-1]
            #Split the line at all the commas
            line = line.split(',')
            dict = {}
            for element in line:
                if element in dict:
                    dict[element] += 1
                else:
                    dict[element] = 1
            moves.append(dict)
    return moves

def remove_illegal(moves, df):
    for i in range(len(moves)):
        board = chess.Board(df['FEN'][i])
        legal_moves = gen_legal_moves(board)
        if moves[i] not in legal_moves:
            moves[i] = None
    return moves

def get_ensemble_output_dict_varried_size(N):
    moves = []
    with open("ensemble_output.txt", "r") as file:
        for line in file:
            # Remove everything before the first : and the space after
            line = line[line.find(':')+1:]
            # Remove the newline character
            line = line[:-1]
            # Split the line at all the commas
            line = line.split(',')
            dict = {}
            if len(line) <= N:
                for element in line:
                    if element in dict:
                        dict[element] += 1
                    else:
                        dict[element] = 1  
            else:
                for i in range(N):
                    if line[i] in dict:
                        dict[line[i]] += 1
                    else:
                        dict[line[i]] = 1
            moves.append(dict)
            
    return remove_illegal(moves)

def get_ensemble_output_varried_size(N):
    d_moves = get_ensemble_output_dict_varried_size(N)
    moves = []
    #Loop through all dicts in moves, append the key with the highest value to moves_played
    for dict in d_moves:
        max_key = max(dict, key=dict.get)
        moves.append(max_key)
    return moves

def get_ensemble_output():
    d_moves = get_ensemble_output_dict()
    moves = []
    #Loop through all dicts in moves, append the key with the highest value to moves_played
    for dict in d_moves:
        max_key = max(dict, key=dict.get)
        moves.append(max_key)
    return moves

def remove_illegal(moves, df):
    for i in range(len(moves)):
        board = chess.Board(df['FEN'][i])
        legal_moves = gen_legal_moves(board)
        if moves[i] not in legal_moves:
            moves[i] = None
    return moves

def get_ensemble_output_dict_varried_size(N):
    moves = []
    with open("ensemble_output.txt", "r") as file:
        for line in file:
            # Remove everything before the first : and the space after
            line = line[line.find(':')+1:]
            # Remove the newline character
            line = line[:-1]
            # Split the line at all the commas
            line = line.split(',')
            dict = {}
            if len(line) <= N:
                for element in line:
                    if element in dict:
                        dict[element] += 1
                    else:
                        dict[element] = 1  
            else:
                for i in range(N):
                    if line[i] in dict:
                        dict[line[i]] += 1
                    else:
                        dict[line[i]] = 1
            moves.append(dict)
    return moves

def get_ensemble_output_varried_size(N):
    d_moves = get_ensemble_output_dict_varried_size(N)
    moves = []
    #Loop through all dicts in moves, append the key with the highest value to moves_played
    for dict in d_moves:
        max_key = max(dict, key=dict.get)
        moves.append(max_key)
    return remove_illegal(moves,df)
