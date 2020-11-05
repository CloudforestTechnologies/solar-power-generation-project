'''
load_data

This file supports loading project data into memory.

'''

# Module importations
import pandas as pd

# Constants
LOAD_DIRECTORY = r'C:/Developer/solar-power-generation-project/Data/Raw'

def load_data(filename):
    """Load Dataset
    ======================================
    Loads dataset from user-specified directory.
    
    Args:
        filename (Str) - Name of csv file.
        
    Returns:
        dataframe (dataframe) - Dataframe loaded with data from csv.
    """

    file_string = LOAD_DIRECTORY + '/' + filename

    return pd.read_csv(file_string)