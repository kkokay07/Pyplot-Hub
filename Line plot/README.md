# Line Plot Generator

A Python script for generating publication-quality line plots from tabulated data. The script creates plots with multiple lines, a translucent grid background, and an external legend.

## Features

- Handles multiple data columns automatically
- Customizable plot title and resolution
- External legend positioned on the right side
- Translucent grid lines in the background
- Professional-looking output suitable for publications
- Flexible input handling for any number of columns
- Command-line interface with intuitive flags

## Prerequisites

Required Python packages:
```bash
matplotlib
pandas
```

Install dependencies using pip:
```bash
pip install matplotlib pandas
```

## Input File Format

The input file should be a tab-separated text file (.txt) with:
- First row containing column headers
- First column containing x-axis values (e.g., generations, time points)
- Subsequent columns containing y-axis values for different series

Example input file format:
```
Generation    ASI     AST     AMI     AfT
1            242.916  34.152  39.7611 206.445
2            242.916  34.152  39.7611 206.445
3            242.916  34.152  39.7611 206.445
4            242.916  19.5424 39.7611 206.445
```

## Usage

Basic usage:
```bash
python3 plot_script.py --input data.txt --title "My Plot Title" --dpi 300
```

Command-line options:
```
--input, -i : Input file path (required)
--title, -t : Plot title (required)
--dpi, -d   : Resolution of output image (optional, default: 300)
```

Short form flags are also supported:
```bash
python3 plot_script.py -i data.txt -t "My Plot Title" -d 300
```

## Output

The script generates:
- A PNG file named 'line_plot.png' in the current directory
- Plot features:
  - Multiple colored lines for each data column
  - Legend positioned outside the plot on the right
  - Translucent grid lines in the background
  - Clear axis labels and title
  - Professional formatting suitable for publications

## Usage:
```bash
python3 lineplot.py --input data.txt --title "Your Title Goes Here" --dpi 600
```
Example of Input Format: 
Series    Pop1    Pop2    Pop3    Pop4    Pop5
1            242.9   34.1    39.7    206.4   488.4
2            242.9   34.1    39.7    206.4   488.4
3            242.9   34.1    39.7    206.4   488.4

Values are separated by tabs
Each row has the same number of columns
First column contains increasing values
No missing values


## Troubleshooting

Common issues and solutions:

1. **File Not Found Error**
   - Ensure the input file path is correct
   - Check if you have read permissions for the file

2. **Invalid File Format**
   - Verify the input file is tab-separated
   - Ensure all columns have headers
   - Check for missing or malformed data

3. **Memory Issues with Large Files**
   - Try reducing the DPI value
   - Ensure sufficient system memory is available

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
