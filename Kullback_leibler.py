import numpy as np
import seaborn as sns
import pandas as pd
from stockfish import Stockfish
import chess
import math
import random
from evaluation_pipeline_copy import *
from plot_functions import *
from scipy.special import rel_entr

import matplotlib.pyplot as plt
import chess.engine


# Load the data
df = pd.read_csv(r"chessData.csv")

# Generate synthetic data
data = generate_synthetic_data_dict(10,1,df,1)

# Calculate the scores
moves = generate_synthetic_data_dict(10,4,df,1)
scores = ensemble_score(moves, df)
stockfish_score = stockfish_score_function(data, df)

# Plot the distribution
x_grid1, kde_values_ensemble = distribution_plot(scores)
x_grid2, kde_values_stockfish = distribution_plot(stockfish_score)

x_grid1, kde_values_ensemble, x_grid2, kde_values_stockfish = distribution_plot(scores, stockfish_score)

# Calculate the KL divergence
KL = sum(rel_entr(kde_values_stockfish, kde_values_ensemble))
print(KL)