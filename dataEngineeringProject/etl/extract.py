# extract data 
#   - check if file exists and is readable
#   - extract data from xlsx file 

import pandas as pd
import os 

def extract_data(file_path):
    """Extract data from xlsx file

    Args:
        file_path (str): path to xlsx file

    Returns:
        pandas.DataFrame: dataframe of data
    """
    
    # initialize dataframe
    extract_df = pd.DataFrame()

    # check if file exists and is redable
    if os.access(file_path, os.R_OK):
        extract_df = pd.read_excel(file_path, sheet_name='DATA', header=0)
        return extract_df
    else:
        print("File is not accessible")
        extract_df = None
        return extract_df

if __name__ == "__main__":
    # check if file exists and is readable
    if os.access('./data/raw/DEM_Challenge_Section1_DATASET.xlsx', os.R_OK):
        extract_df = extract_data('./data/raw/DEM_Challenge_Section1_DATASET.xlsx')
        print(extract_df.columns)
    else:
        print("File is not accessible")

