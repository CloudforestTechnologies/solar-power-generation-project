'''
data_munging

This file supports data cleaning and preprocessing operations.
'''

# Module Importations
import pandas as pd
from dateutil import parser

def return_datetime_id(datetime_string):
    """Return Datetime Id
    ======================================
    Returns a datetime id based on date and time from data instance.
    
    Args:
        datetime_string (str) - Datetime as a string object.
        
    Returns:
        datetime_id (str) - Datetime (UTC) stamp returned as a string.
    """

    # Convert to datetime
    datetime_date = parser.parse(datetime_string)

    # Return datetime
    return datetime_date