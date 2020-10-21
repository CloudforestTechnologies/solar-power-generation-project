'''
data_munging

This file supports data cleaning and preprocessing operations.
'''

# Module Importations
import datetime
import pandas as pd

def return_datetime(datetime_string):
    """Return Datetime
    ======================================
    Returns a datetime based on date and time from data instance.
    
    Args:
        datetime_string (str) - Datetime as a string object.
        
    Returns:
        datetime (DateTime) - DateTime object corresponding to date and time.
    """

    # Convert to datetime
    datetime_date = datetime.datetime.strptime(datetime_string, '%d-%m-%Y %H:%M')

    # Return datetime
    return datetime_date

def return_cell_number(source_key):
    """Return Cell Number
    ======================================
    Returns a cell number based on a Source Key value used with a dict.
    
    Args:
        source_key (str) - Source key for the .
        
    Returns:
        cell_number (int) - Cell number as an integer.
    """

    pass