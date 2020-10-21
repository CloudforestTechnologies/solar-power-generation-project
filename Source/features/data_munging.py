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
        cell_number (str) - Cell number as a string.
    """

    # Source Key - Cell Number dictionary
    cell_number_dict = {
        '1BY6WEcLGh8j5v7' : '1', '1IF53ai7Xc0U56Y' : '2', '3PZuoBAID5Wc2HD' : '3', '7JYdWkrLSPkdwr4' : '3',
        'McdE0feGgRqW7Ca' : '5', 'VHMLBKoKgIrUVDU' : '6', 'WRmjgnKYAwPKWDb' : '7', 'ZnxXDlPa8U1GXgE' : '8',
        'ZoEaEvLYb1n2sOq' : '9', 'adLQvlD726eNBSB' : '10', 'bvBOhCH3iADSZry' : '11', 'iCRJl6heRkivqQ3' : '12',
        'ih0vzX44oOqAx2f' : '13', 'pkci93gMrogZuBj' : '14', 'rGa61gmuvPhdLxV' : '15', 'sjndEbLyjtCKgGv' : '16',
        'uHbuxQJl8lW7ozc' : '17', 'wCURE6d3bPkepu2' : '18', 'z9Y9gH1T5YWrNuG' : '19', 'zBIq5rxdHJRwDNY' : '20',
        }

    # Try to find cell number in dict
    try:
        cell_number = cell_number_dict(source_key)
    except:
        cell_number = ""

    # Return cell number