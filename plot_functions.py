import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def bar_plot(categories, counts, N, xlabel, ylabel, title, width=0.5, color='skyblue'):
    # Create the bar plot
    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, counts, color=color, width=width)
    
    percentages = [count / N * 100 for count in counts]
    # Add percentage labels on top of each bar
    for bar, percentage in zip(bars, percentages):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage:.2f}%', ha='center', va='bottom')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def distribution_plot(data):
    # Create KDE
    kde = gaussian_kde(data, bw_method=0.5)
    
    # Evaluate KDE on a grid
    x_grid = np.linspace(min(data), max(data), 1000)
    kde_values = kde(x_grid)
    
    # Plot KDE
    sns.kdeplot(data, bw_adjust=0.5, fill=True)
    
    # Plot histogram
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Set plot labels and title
    plt.xlabel('Values')
    plt.ylabel('Probability Density')
    plt.title('Non-Parametric Probability Distribution (KDE)')
    
    # Display plot
    plt.show()
    
    # Return the grid and corresponding KDE values
    return x_grid, kde_values