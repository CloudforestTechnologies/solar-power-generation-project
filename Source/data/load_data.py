'''
load_data

This file supports loading project data into memory.

'''

# Module importations
import pandas as pd

# Constants
LOAD_DIRECTORY = r'C:/Developer/solar-power-generation-project/Data/Raw'
PICKLE_DIRECTORY = r'C:/Developer/solar-power-generation-project/Data/Interim'

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

def pickle_data(input_dataframe, filename):
    """Pickle Data
    ======================================
    Pickles data into a dataframe saved in user-specified directory.
    
    Args:
        input_dataframe (dataframe) - Dataframe to be pickled.
        filename (str) - Name of pickled file.
        
    Returns:
        None.
    """

    # Build pickle string
    pickle_string = PICKLE_DIRECTORY + "/" + filename + ".pkl"

    # Pickle dataframe
    input_dataframe.to_pickle(pickle_string)

    print("Pickled dataframe to: " + pickle_string)

def load_pickled_data(pickled_filename):
    """Load Pickled Data
    ======================================
    Loads pickled data from Interim folder into a returned dataframe.
    
    Args:
        pickled_filename (str) - Name of pickled file.
        
    Returns:
        dataframe (dataframe) - Dataframe loaded with data from pickle.
    """

    # Build load string
    load_string = PICKLE_DIRECTORY + '/' + pickled_filename

    # Load data into dataframe
    df_loaded = pd.read_pickle(load_string)

    print("Loaded pickled dataframe ...")

    # Return dataframe
    return df_loaded