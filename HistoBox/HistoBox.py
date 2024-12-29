import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import argparse

def create_box_histogram(data, title, output_file, dpi=600):
    """Create combined box plot and histogram for each group"""
    # Number of groups
    n_groups = len(data.columns)
    
    # Set up colors for different groups - using pastel colors
    colors = ['#B3E2CD', '#FDCDAC', '#CBD5E8', '#F4CAE4', '#E6F5C9',
              '#FFF2AE', '#F1E2CC', '#CCCCCC', '#E41A1C', '#377EB8',
              '#4DAF4A', '#984EA3'][:n_groups]
    
    # Create figure
    fig = plt.figure(figsize=(15, 8))
    
    # Create grid layout
    gs = GridSpec(1, n_groups, figure=fig)
    
    # Create subplots for each group
    for idx, column in enumerate(data.columns):
        group_data = data[column].dropna()
        
        # Create subplot
        ax = fig.add_subplot(gs[0, idx])
        
        # Add histogram on the left
        hist_heights, bins = np.histogram(group_data, bins=15, density=True)
        hist_heights = hist_heights / np.max(hist_heights) * 0.5  # Normalize height
        ax.barh(y=(bins[:-1] + bins[1:])/2, width=hist_heights, 
                height=np.diff(bins), color=colors[idx],
                align='center')
        
        # Add box plot on the right
        box_position = 0.7
        bp = ax.boxplot(group_data, positions=[box_position], 
                       vert=True, patch_artist=True,
                       widths=0.15,
                       flierprops=dict(marker='o', markerfacecolor=colors[idx],
                                     markeredgecolor=colors[idx], markersize=3))
        
        # Customize box plot appearance
        plt.setp(bp['boxes'], facecolor=colors[idx])
        plt.setp(bp['medians'], color='black', linewidth=1)
        plt.setp(bp['whiskers'], color='black', linewidth=1)
        plt.setp(bp['caps'], color='black', linewidth=1)
        
        # Set title and labels
        ax.set_title(column, pad=10)
        
        # Set axis limits
        data_range = group_data.max() - group_data.min()
        ax.set_xlim(-0.1, 1)
        ax.set_ylim(group_data.min() - data_range*0.1,
                   group_data.max() + data_range*0.1)
        
        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Show y-axis only for first subplot
        if idx > 0:
            ax.set_yticklabels([])
        
        # Remove x-axis labels
        ax.set_xticks([])
    
    # Add overall title
    plt.suptitle(title, size=14, y=1.05)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(output_file, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close()

    # Print statistics
    print("\nSummary Statistics:")
    stats_df = data.describe()
    print(stats_df.round(6).to_string())

def main():
    parser = argparse.ArgumentParser(description='Create box plot with histogram')
    parser.add_argument('--input', required=True, help='Input file path (tab-separated)')
    parser.add_argument('--title', required=True, help='Plot title')
    parser.add_argument('--output', required=True, help='Output file path')
    parser.add_argument('--dpi', type=int, default=600, help='Output DPI')
    
    args = parser.parse_args()
    
    try:
        # Read data
        data = pd.read_csv(args.input, sep='\t')
        
        # Create plot
        create_box_histogram(data, args.title, args.output, args.dpi)
        
        print(f"Plot saved successfully as {args.output}")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
