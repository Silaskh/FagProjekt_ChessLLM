import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def bar_plot(categories, p1, p2, N, xlabel="Percentage of legal moves given", ylabel="Number of legal moves taken", title="Number of legal moves", label1 = "Llama2", label2="Llama3", width=0.4, color1= "teal", color2="turquoise"):
    # Calculate positions of bars
    bar_width = width / 2
    positions1 = [i - bar_width for i in range(len(categories))]
    positions2 = [i + bar_width for i in range(len(categories))]
    
    # Create the bar plot
    plt.figure(figsize=(10, 6))
    bars1 = plt.bar(positions1, [p*N for p in p1], color=color1, width=width, label=label1)
    bars2 = plt.bar(positions2, [p*N for p in p2], color=color2, width=width, label=label2)
    
    # Add percentage labels on top of each bar
    for bar1, p1_value in zip(bars1, p1):
        height = bar1.get_height()
        plt.text(bar1.get_x() + bar1.get_width() / 2, height, f'{p1_value:.2f}%', ha='center', va='bottom')
    
    for bar2, p2_value in zip(bars2, p2):
        height = bar2.get_height()
        plt.text(bar2.get_x() + bar2.get_width() / 2, height, f'{p2_value:.2f}%', ha='center', va='bottom')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(range(len(categories)), categories)
    plt.legend()
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
    

def distribution_plot_dict(data_dict, xlabel='Scores', ylabel='Probability Density', title='Non-Parametric Probability Distribution (KDE)'):
    plt.figure(figsize=(10, 6))
    
    for label, data in data_dict.items():
        kde = gaussian_kde(data, bw_method=0.5)
        x_grid = np.linspace(min(data), max(data), 1000)
        kde_values = kde(x_grid)
        
        # Plot KDE
        sns.kdeplot(data, bw_adjust=0.5, fill=True)
    
    # Set plot labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

# Example usage
# data1 = np.random.normal(0, 1, 10000)
# data2 = np.random.normal(1, 1, 10000)
# data3 = np.random.normal(2, 1, 10000)

# data_dict = {
#     'Data 1': data1,
#     'Data 2': data2,
#     'Data 3': data3
# }

# distribution_plot(data_dict)


    


