import matplotlib.pyplot as plt
import pandas as pd
import argparse

def create_line_plot(input_file, plot_title, dpi=300):
    # Read data
    df = pd.read_csv(input_file, sep='\t')
    
    # Create figure and axis with specific size
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Get x-axis values (first column)
    x_column = df.columns[0]
    x_values = df[x_column]
    
    # Plot each column except the first one
    for column in df.columns[1:]:
        ax.plot(x_values, df[column], label=column, linewidth=2)
    
    # Customize the plot
    ax.set_xlabel(x_column, fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title(plot_title, fontsize=14, pad=20)
    
    # Add grid with transparency
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)  # Place grid behind the lines
    
    # Customize ticks
    ax.tick_params(axis='both', which='major', labelsize=10)
    
    # Add legend outside the plot
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', 
             fontsize=10, frameon=True)
    
    # Adjust layout to prevent legend cutoff
    plt.tight_layout()
    
    # Save plot
    output_file = 'line_plot.png'
    plt.savefig(output_file, dpi=dpi, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved as {output_file}")

def main():
    # Create parser
    parser = argparse.ArgumentParser(description='Create a line plot from tabulated data')
    
    # Add arguments
    parser.add_argument('--input', '-i', 
                        required=True,
                        help='Input file path (tab-separated)')
    parser.add_argument('--title', '-t',
                        required=True,
                        help='Plot title')
    parser.add_argument('--dpi', '-d',
                        type=int,
                        default=300,
                        help='DPI for output image (default: 300)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create plot
    create_line_plot(args.input, args.title, args.dpi)

if __name__ == "__main__":
    main()
