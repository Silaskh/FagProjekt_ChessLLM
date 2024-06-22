import pickle as pkl
import ast

with open('move_difference_2_1350.pkl', 'rb') as file:
    move_data_2_1350 = pkl.load(file)
    score_difference_2_1350 = move_data_2_1350['score_difference']
    moves_df_list_2_1350 = move_data_2_1350['moves_df_list']
    move_scores_2_1350 = move_data_2_1350['move_scores']
    
with open('move_difference_2_1800.pkl', 'rb') as file:
    move_data_2_1800 = pkl.load(file)
    score_difference_2_1800 = move_data_2_1800['score_difference']
    moves_df_list_2_1800 = move_data_2_1800['moves_df_list']
    move_scores_2_1800 = move_data_2_1800['move_scores']

with open('move_difference_2_2250.pkl', 'rb') as file:
    move_data_2_2250 = pkl.load(file)
    score_difference_2_2250 = move_data_2_2250['score_difference']
    moves_df_list_2_2250 = move_data_2_2250['moves_df_list']
    move_scores_2_2250 = move_data_2_2250['move_scores']
    
with open('move_difference_2_2700.pkl', 'rb') as file:
    move_data_2_2700 = pkl.load(file)
    score_difference_2_2700 = move_data_2_2700['score_difference']
    moves_df_list_2_2700 = move_data_2_2700['moves_df_list']
    move_scores_2_2700 = move_data_2_2700['move_scores']
    
with open('move_difference_2_3150.pkl', 'rb') as file:
    move_data_2_3150 = pkl.load(file)
    score_difference_2_3150 = move_data_2_3150['score_difference']
    moves_df_list_2_3150 = move_data_2_3150['moves_df_list']
    move_scores_2_3150 = move_data_2_3150['move_scores']
    
with open('move_difference_3_1350.pkl', 'rb') as file:
    move_data_3_1350 = pkl.load(file)
    score_difference_3_1350 = move_data_3_1350['score_difference']
    moves_df_list_3_1350 = move_data_3_1350['moves_df_list']
    move_scores_3_1350 = move_data_3_1350['move_scores']
    
with open('move_difference_3_1800.pkl', 'rb') as file:
    move_data_3_1800 = pkl.load(file)
    score_difference_3_1800 = move_data_3_1800['score_difference']
    moves_df_list_3_1800 = move_data_3_1800['moves_df_list']
    move_scores_3_1800 = move_data_3_1800['move_scores']
    
with open('move_difference_3_2250.pkl', 'rb') as file:
    move_data_3_2250 = pkl.load(file)
    score_difference_3_2250 = move_data_3_2250['score_difference']
    moves_df_list_3_2250 = move_data_3_2250['moves_df_list']
    move_scores_3_2250 = move_data_3_2250['move_scores']

with open('move_difference_3_2700.pkl', 'rb') as file:
    move_data_3_2700 = pkl.load(file)
    score_difference_3_2700 = move_data_3_2700['score_difference']
    moves_df_list_3_2700 = move_data_3_2700['moves_df_list']
    move_scores_3_2700 = move_data_3_2700['move_scores']
    
with open('move_difference_3_3150.pkl', 'rb') as file:
    move_data_3_3150 = pkl.load(file)
    score_difference_3_3150 = move_data_3_3150['score_difference']
    moves_df_list_3_3150 = move_data_3_3150['moves_df_list']
    move_scores_3_3150 = move_data_3_3150['move_scores']
    
with open('move_difference_ensemble_1350.pkl', 'rb') as file:
    move_data_ensemble_1350 = pkl.load(file)
    score_difference_ensemble_1350 = move_data_ensemble_1350['score_difference']
    moves_df_list_ensemble_1350 = move_data_ensemble_1350['moves_df_list']
    move_scores_ensemble_1350 = move_data_ensemble_1350['move_scores']
    
with open('move_difference_ensemble_1800.pkl', 'rb') as file:
    move_data_ensemble_1800 = pkl.load(file)
    score_difference_ensemble_1800 = move_data_ensemble_1800['score_difference']
    moves_df_list_ensemble_1800 = move_data_ensemble_1800['moves_df_list']
    move_scores_ensemble_1800 = move_data_ensemble_1800['move_scores']
    
with open('move_difference_ensemble_2250.pkl', 'rb') as file:
    move_data_ensemble_2250 = pkl.load(file)
    score_difference_ensemble_2250 = move_data_ensemble_2250['score_difference']
    moves_df_list_ensemble_2250 = move_data_ensemble_2250['moves_df_list']
    move_scores_ensemble_2250 = move_data_ensemble_2250['move_scores']
    
with open('move_difference_ensemble_2700.pkl', 'rb') as file:
    move_data_ensemble_2700 = pkl.load(file)
    score_difference_ensemble_2700 = move_data_ensemble_2700['score_difference']
    moves_df_list_ensemble_2700 = move_data_ensemble_2700['moves_df_list']
    move_scores_ensemble_2700 = move_data_ensemble_2700['move_scores']
    
with open('move_difference_ensemble_3150.pkl', 'rb') as file:
    move_data_ensemble_3150 = pkl.load(file)
    score_difference_ensemble_3150 = move_data_ensemble_3150['score_difference']
    moves_df_list_ensemble_3150 = move_data_ensemble_3150['moves_df_list']
    move_scores_ensemble_3150 = move_data_ensemble_3150['move_scores']
    
with open('move_difference_random_1350.pkl', 'rb') as file:
    move_data_random_1350 = pkl.load(file)
    score_difference_random_1350 = move_data_random_1350['score_difference']
    moves_df_list_random_1350 = move_data_random_1350['moves_df_list']
    move_scores_random_1350 = move_data_random_1350['move_scores']
    
with open('move_difference_random_1800.pkl', 'rb') as file:
    move_data_random_1800 = pkl.load(file)
    score_difference_random_1800 = move_data_random_1800['score_difference']
    moves_df_list_random_1800 = move_data_random_1800['moves_df_list']
    move_scores_random_1800 = move_data_random_1800['move_scores']
    
with open('move_difference_random_2250.pkl', 'rb') as file:
    move_data_random_2250 = pkl.load(file)
    score_difference_random_2250 = move_data_random_2250['score_difference']
    moves_df_list_random_2250 = move_data_random_2250['moves_df_list']
    move_scores_random_2250 = move_data_random_2250['move_scores']
    
with open('move_difference_random_2700.pkl', 'rb') as file:
    move_data_random_2700 = pkl.load(file)
    score_difference_random_2700 = move_data_random_2700['score_difference']
    moves_df_list_random_2700 = move_data_random_2700['moves_df_list']
    move_scores_random_2700 = move_data_random_2700['move_scores']
    
with open('move_difference_random_3150.pkl', 'rb') as file:
    move_data_random_3150 = pkl.load(file)
    score_difference_random_3150 = move_data_random_3150['score_difference']
    moves_df_list_random_3150 = move_data_random_3150['moves_df_list']
    move_scores_random_3150 = move_data_random_3150['move_scores']
    
with open('counts_random_1350.txt', 'r') as file:
    counts_random_1350_str = file.read()

    # remove the index and open the last array in the file as variable counts_random_1350
    counts_random_1350_str = (counts_random_1350_str.replace('118:', '')).replace('.',',')
    counts_random_1350 = ast.literal_eval(counts_random_1350_str.split('\n')[-2])

with open('counts_random_1800.txt', 'r') as file:
    counts_random_1800_str = file.read()

    # remove the index and open the last array in the file as variable counts_random_1800
    counts_random_1800_str = (counts_random_1800_str.replace('118:', '')).replace('.',',')
    counts_random_1800 = ast.literal_eval(counts_random_1800_str.split('\n')[-2])
    
with open('counts_random_2250.txt', 'r') as file:
    counts_random_2250_str = file.read()

    # remove the index and open the last array in the file as variable counts_random_2250
    counts_random_2250_str = (counts_random_2250_str.replace('118:', '')).replace('.',',')
    counts_random_2250 = ast.literal_eval(counts_random_2250_str.split('\n')[-2])
    
with open('counts_random_2700.txt', 'r') as file:
    counts_random_2700_str = file.read()

    # remove the index and open the last array in the file as variable counts_random_2700
    counts_random_2700_str = (counts_random_2700_str.replace('118:', '')).replace('.',',')
    counts_random_2700 = ast.literal_eval(counts_random_2700_str.split('\n')[-2])
    
with open('counts_random_3150.txt', 'r') as file:
    counts_random_3150_str = file.read()

    # remove the index and open the last array in the file as variable counts_random_3150
    counts_random_3150_str = (counts_random_3150_str.replace('118:', '')).replace('.',',')
    counts_random_3150 = ast.literal_eval(counts_random_3150_str.split('\n')[-2])

with open('counts_ensemble_1350.txt', 'r') as file:
    counts_ensemble_1350_str = file.read()

    # remove the index and open the last array in the file as variable counts_ensemble_1350
    counts_ensemble_1350_str = (counts_ensemble_1350_str.replace('118:', '')).replace('.',',')
    counts_ensemble_1350 = ast.literal_eval(counts_ensemble_1350_str.split('\n')[-2])
    
with open('counts_ensemble_1800.txt', 'r') as file:
    counts_ensemble_1800_str = file.read()

    # remove the index and open the last array in the file as variable counts_ensemble_1800
    counts_ensemble_1800_str = (counts_ensemble_1800_str.replace('118:', '')).replace('.',',')
    counts_ensemble_1800 = ast.literal_eval(counts_ensemble_1800_str.split('\n')[-2])
    
with open('counts_ensemble_2250.txt', 'r') as file:
    counts_ensemble_2250_str = file.read()

    # remove the index and open the last array in the file as variable counts_ensemble_2250
    counts_ensemble_2250_str = (counts_ensemble_2250_str.replace('118:', '')).replace('.',',')
    counts_ensemble_2250 = ast.literal_eval(counts_ensemble_2250_str.split('\n')[-2])
    
with open('counts_ensemble_2700.txt', 'r') as file:
    counts_ensemble_2700_str = file.read()

    # remove the index and open the last array in the file as variable counts_ensemble_2700
    counts_ensemble_2700_str = (counts_ensemble_2700_str.replace('118:', '')).replace('.',',')
    counts_ensemble_2700 = ast.literal_eval(counts_ensemble_2700_str.split('\n')[-2])
    
with open('counts_ensemble_3150.txt', 'r') as file:
    counts_ensemble_3150_str = file.read()

    # remove the index and open the last array in the file as variable counts_ensemble_3150
    counts_ensemble_3150_str = (counts_ensemble_3150_str.replace('118:', '')).replace('.',',')
    counts_ensemble_3150 = ast.literal_eval(counts_ensemble_3150_str.split('\n')[-2])
    
with open('counts_2_1350.txt', 'r') as file:
    counts_2_1350_str = file.read()

    # remove the index and open the last array in the file as variable counts_2_1350
    counts_2_1350_str = (counts_2_1350_str.replace('118:', '')).replace('.',',')
    counts_2_1350 = ast.literal_eval(counts_2_1350_str.split('\n')[-2])
    
with open('counts_2_1800.txt', 'r') as file:
    counts_2_1800_str = file.read()

    # remove the index and open the last array in the file as variable counts_2_1800
    counts_2_1800_str = (counts_2_1800_str.replace('118:', '')).replace('.',',')
    counts_2_1800 = ast.literal_eval(counts_2_1800_str.split('\n')[-2])
    
with open('counts_2_2250.txt', 'r') as file:
    counts_2_2250_str = file.read()

    # remove the index and open the last array in the file as variable counts_2_2250
    counts_2_2250_str = (counts_2_2250_str.replace('118:', '')).replace('.',',')
    counts_2_2250 = ast.literal_eval(counts_2_2250_str.split('\n')[-2])
    
with open('counts_2_2700.txt', 'r') as file:
    counts_2_2700_str = file.read()

    # remove the index and open the last array in the file as variable counts_2_2700
    counts_2_2700_str = (counts_2_2700_str.replace('118:', '')).replace('.',',')
    counts_2_2700 = ast.literal_eval(counts_2_2700_str.split('\n')[-2])
    
with open('counts_2_3150.txt', 'r') as file:
    counts_2_3150_str = file.read()

    # remove the index and open the last array in the file as variable counts_2_3150
    counts_2_3150_str = (counts_2_3150_str.replace('118:', '')).replace('.',',')
    counts_2_3150 = ast.literal_eval(counts_2_3150_str.split('\n')[-2])
    
with open('counts_3_1350.txt', 'r') as file:
    counts_3_1350_str = file.read()

    # remove the index and open the last array in the file as variable counts_3_1350
    counts_3_1350_str = (counts_3_1350_str.replace('118:', '')).replace('.',',')
    counts_3_1350 = ast.literal_eval(counts_3_1350_str.split('\n')[-2])
    
with open('counts_3_1800.txt', 'r') as file:
    counts_3_1800_str = file.read()

    # remove the index and open the last array in the file as variable counts_3_1800
    counts_3_1800_str = (counts_3_1800_str.replace('118:', '')).replace('.',',')
    counts_3_1800 = ast.literal_eval(counts_3_1800_str.split('\n')[-2])
    
with open('counts_3_2250.txt', 'r') as file:
    counts_3_2250_str = file.read()

    # remove the index and open the last array in the file as variable counts_3_2250
    counts_3_2250_str = (counts_3_2250_str.replace('118:', '')).replace('.',',')
    counts_3_2250 = ast.literal_eval(counts_3_2250_str.split('\n')[-2])

with open('counts_3_2700.txt', 'r') as file:
    counts_3_2700_str = file.read()

    # remove the index and open the last array in the file as variable counts_3_2700
    counts_3_2700_str = (counts_3_2700_str.replace('118:', '')).replace('.',',')
    counts_3_2700 = ast.literal_eval(counts_3_2700_str.split('\n')[-2])

with open('counts_3_3150.txt', 'r') as file:
    counts_3_3150_str = file.read()

    # remove the index and open the last array in the file as variable counts_3_3150
    counts_3_3150_str = (counts_3_3150_str.replace('118:', '')).replace('.',',')
    counts_3_3150 = ast.literal_eval(counts_3_3150_str.split('\n')[-2])
