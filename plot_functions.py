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

def distribution_plot(data1, data2=None, label1='Data 1', label2='Data 2', xlabel='Scores', ylabel='Probability Density', title='Non-Parametric Probability Distribution (KDE)', color1='skyblue', color2='pink'):
    # Create KDE
    if data2 is None:
        kde = gaussian_kde(data1, bw_method=0.5)
        
        # Evaluate KDE on a grid
        x_grid = np.linspace(min(data1), max(data1), 1000)
        kde_values = kde(x_grid)
        
        # Plot KDE
        sns.kdeplot(data1, bw_adjust=0.5, fill=True, color=color1)

        
        # Set plot labels and title
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

        return x_grid, kde_values
    
    else:
        kde1 = gaussian_kde(data1, bw_method=0.5)
        kde2 = gaussian_kde(data2, bw_method=0.5) 
        
        # Evaluate KDE on a grid
        x_grid1 = np.linspace(min(data1), max(data1), 1000)
        x_grid2 = np.linspace(min(data2), max(data2), 1000) 
        kde_values1 = kde1(x_grid1)
        kde_values2 = kde2(x_grid2)
        
        # Plot KDE
        sns.kdeplot(data1, bw_adjust=0.5, fill=True, color=color1)
        sns.kdeplot(data2, bw_adjust=0.5, fill=True, color=color2) 

        
        # Set plot labels and title
        plt.xlabel('Values')
        plt.ylabel('Probability Density')
        plt.title('Non-Parametric Probability Distribution (KDE)')
        plt.legend([label1, label2]) 
        return x_grid1, kde_values1, x_grid2, kde_values2