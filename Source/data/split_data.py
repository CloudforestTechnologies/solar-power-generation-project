'''
split_data

This file supports splitting data into development and validation sets, ensuring randomisation of the sets and the same distribution on each occurence.
'''

# Module Importations
import numpy as np
import pandas as pd

def split_train_eval(data, split_ratio):
    """Split Training & Evaluation Data
    ======================================
    Splits original dataset into training and evaluation data.
    
    Args:
        data (dataframe) - Original test data.
        split_ratio (int) - Ratio for splitting dataset as training fraction.
        
    Returns:
        data_train (dataframe) - Dataframe with training data slice.
        data_eval (dataframe) - Dataframe with evaluation data slice.
    """

    # Random seed setting ensures identical data split between calls
    np.random.seed(42)
    shuffled_indices = np.random.permutation(len(data))

    train_set_size = int(len(data) * split_ratio)

    # Create slices of training and evaluation indices
    train_indices = shuffled_indices[train_set_size:]
    eval_indices = shuffled_indices[:train_set_size]

    return data.iloc[train_indices], data.iloc[eval_indices]
