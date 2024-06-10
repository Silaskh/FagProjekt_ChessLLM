import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def bar_plot(categories, counts, N):
    # Create the bar plot
    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, counts)
    
    percentages = [count / N * 100 for count in counts]
    # Add percentage labels on top of each bar
    for bar, percentage in zip(bars, percentages):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage:.2f}%', ha='center', va='bottom')

    plt.xlabel('Percentile')
    plt.ylabel('Number of Moves')
    plt.title('Number of moves in each percentile range of the dataset')
    plt.show()

def distribution_plot(data):
    sns.kdeplot(data, bw_adjust=0.5, fill=True)
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
    plt.xlabel('Values')
    plt.ylabel('Probability Density')
    plt.title('Non-Parametric Probability Distribution (KDE)')
    plt.show()