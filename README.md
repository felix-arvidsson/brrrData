![data processor go brrr](brrr.png)
# Data Processing Script

python script I use for work to process data from excel files.
I will add more features in the future as I need them
 

## Features

- **Remove Duplicate Rows**: Remove duplicate rows based on selected columns.
- **Save Only Duplicates**: Save only the duplicate rows to a new file.
- **Compare Columns**: Compare columns from two files and optionally save common values.
- **List Duplicates**: List duplicate rows in a file and save them if required.
- **Sort Rows**: Sort rows in an Excel file based on a selected column.
- **Modify Column**: Modify values in a selected column with various text manipulation options.

## Installation

   ```sh
   git clone git@github.com:felix-arvidsson/brrrDataProcessor.git
   cd ./brrrDataProcessor
   python -m venv venv && source ./venv/bin/activate
   pip install -r requirements.txt
