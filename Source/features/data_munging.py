'''
data_munging

This file supports data cleaning and preprocessing operations.
'''

# Module Importations
import datetime
import pandas as pd

def return_datetime(df_type, datetime_string):
    """Return Datetime
    ======================================
    Returns a datetime based on date and time from data instance.
    
    Args:
        df_type (str) - DataFrame type ('generation' or 'weather') to assist with selecting parse method.
        datetime_string (str) - Datetime as a string object.
        
    Returns:
        datetime (DateTime) - DateTime object corresponding to date and time.
    """

    # Convert to datetime
    if df_type == 'generation':
        datetime_date = datetime.datetime.strptime(datetime_string, '%d-%m-%Y %H:%M')
    elif df_type == 'weather':
        datetime_date = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')

    # Return datetime
    return datetime_date

def return_cell_number(source_key):
    """Return Cell Number
    ======================================
    Returns a cell number based on a Source Key value used with a dict.
    
    Args:
        source_key (str) - Source key for the cell (both plants have same cell key).
        
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
        'zVJPv84UY57bAof' : '21', 'YxYtjZvoooNbGkE' : '22'
        }

    # Try to find cell number in dict
    try:
        cell_number = cell_number_dict[source_key]
    except:
        cell_number = "Not Found"

    # Return cell number
    return cell_number

def return_amb_temp(weather_df, datetime):
    """Return Ambient Temperature
    ======================================
    Returns an ambient temperature retrieved using a datetime key.
    
    Args:
        weather_df (df) - DataFrame containing weather data.
        datetime (datetime) - Datetime as datetime object.
        
    Returns:
        amb_temp (float64) - Ambient temperature corresponding to datetime.
    """

    # Retrieve amb temp from weather df
    amb_temp = weather_df.loc[(weather_df.DATE_TIME == datetime)].AMBIENT_TEMPERATURE.values[0]

    # Return amb temp
    return amb_temp

def combine_generation_weather_dataframes(generation_df, weather_df):
    """Combine Generation & Weather Dataframes
    ======================================
    Returns a dataframe combining generation and weather data.
    
    Args:
        generation_df (dataframe) - Dataframe containing generation data.
        weather_df (dataframe) - Dataframe containing weather data.
        
    Returns:
        combined_df (dataframe) - Dataframe containing combined datasets.
    """

    # Create new df from generation copy
    df_combi = generation_df.copy()

    # Create new column for amb temp using lambda on row and datetime
    df_combi['AMB_TEMP'] = df_combi.apply(lambda row: return_amb_temp(weather_df, row['DATE_TIME']), axis = 1)

    # Create new column for mod temp using lambda on row and datetime

    # Create new column for irradiation using lambda on row and datetime

    # Return dataframe
    return df_combi