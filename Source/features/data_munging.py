'''
data_munging

This file supports data cleaning and preprocessing operations.
'''

# Module Importations
import datetime
from datetime import timedelta
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

def return_time_of_day(datetime_value):
    """Return Time of Day
    ======================================
    Returns a time of day based on time from data instance.
    
    Args:
        datetime_value (DateTime) - Datetime as a datetime object.
        
    Returns:
        time_of_day (DateTime) - DateTime object corresponding to time only.
    """

    # Derive time from datetime
    time_of_day = datetime_value.time()

    # Return time
    return time_of_day

def return_start_end_date(df1, df2):
    """Return Start and End Dates
    ======================================
    Returns Start and End Dates from two dataframes.
    
    Args:
        df1 (Dataframe) - First dataframe.
        df2 (Dataframe) - Second dataframe.
        
    Returns:
        start_datetime (DateTime) - DateTime object for earliest datetime.
        end_datetime (DateTime) - DateTime object for latest datetime.
    """

    # Retrieve earliest datetimes
    df1_min = df1.DATE_TIME.min()
    df2_min = df2.DATE_TIME.min()

    # Compare datetimes, select earliest
    df_min = df1_min
    if df_min > df2_min:
        df_min = df2_min

    # Retrieve latest datetimes
    df1_max = df1.DATE_TIME.max()
    df2_max = df2.DATE_TIME.max()

    # Compare datetimes, select latest
    df_max = df1_max
    if df_max < df2_max:
        df_max = df2_max

    # Return earliest and latest.
    return df_min, df_max

def return_list_of_datetimes(start, end, period = 15):
    """Return List of Datetimes
    ======================================
    Returns list of datetimes periodically spaced between start and end.
    
    Args:
        start (DateTime) - First datetime in list
        end (DateTime) - Last datetime in list
        period (int) - Number of minutes between list entries
        
    Returns:
        datetime_list (DateTime) - List of datetimes running from start to end
    """

    # Convert period to time delta
    period = timedelta(minutes = period)

    # Intialise list
    list_of_datetimes = []
    list_of_datetimes.append(start)

    # Add datetimes to list until end is reached

    # Return list
    return(list_of_datetimes)


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
        '1BY6WEcLGh8j5v7' : '01', '1IF53ai7Xc0U56Y' : '02', '3PZuoBAID5Wc2HD' : '03', '7JYdWkrLSPkdwr4' : '03',
        'McdE0feGgRqW7Ca' : '05', 'VHMLBKoKgIrUVDU' : '06', 'WRmjgnKYAwPKWDb' : '07', 'ZnxXDlPa8U1GXgE' : '08',
        'ZoEaEvLYb1n2sOq' : '09', 'adLQvlD726eNBSB' : '10', 'bvBOhCH3iADSZry' : '11', 'iCRJl6heRkivqQ3' : '12',
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
    try:
        amb_temp = weather_df.loc[(weather_df.DATE_TIME == datetime)].AMBIENT_TEMPERATURE.values[0]

    except:
        amb_temp = 28
        print(datetime, amb_temp)

    # Return amb temp
    return amb_temp

def return_mod_temp(weather_df, datetime):
    """Return Module Temperature
    ======================================
    Returns a module temperature value retrieved using a datetime key.
    
    Args:
        weather_df (df) - DataFrame containing weather data.
        datetime (datetime) - Datetime as datetime object.
        
    Returns:
        mod_temp (float64) - Module temperature corresponding to datetime.
    """

    # Retrieve module temperature from weather df
    try:
        mod_temp = weather_df.loc[(weather_df.DATE_TIME == datetime)].MODULE_TEMPERATURE.values[0]

    except:
        mod_temp = 22
        print(datetime, mod_temp)

    # Return module temperature
    return mod_temp

def return_irradiation(weather_df, datetime):
    """Return Irradiation
    ======================================
    Returns a module irradiation value retrieved using a datetime key.
    
    Args:
        weather_df (df) - DataFrame containing weather data.
        datetime (datetime) - Datetime as datetime object.
        
    Returns:
        irradiation (float64) - Irradiation corresponding to datetime.
    """

    # Retrieve mod temp from weather df
    try:
        irradiation = weather_df.loc[(weather_df.DATE_TIME == datetime)].IRRADIATION.values[0]

    except:
        irradiation = 0
        print(datetime, irradiation)

    # Return mod temp
    return irradiation

def combine_generation_weather_dataframes2(generation_df, weather_df):
    """Combine Generation & Weather Dataframes
    ======================================
    Returns a dataframe combining generation and weather data.
    
    Args:
        generation_df (dataframe) - Dataframe containing generation data.
        weather_df (dataframe) - Dataframe containing weather data.
        
    Returns:
        combined_df (dataframe) - Dataframe containing combined datasets.
    """

    # Determine start & end dates for dataframe
    start, end = return_start_end_date(generation_df, weather_df)

    # Create list of timestamps required as index 

    # Initialise new dataframe with time stamps

    # Iterate over each cell key in dataframe, add generation data (using key and datetime)

    # Iterate over each cell key in dataframe, add weather data (using key and datetime)

    # Create new column for amb temp using lambda on row and datetime
    df_combi['AMB_TEMP'] = df_combi.apply(lambda row: return_amb_temp(weather_df, row['DATE_TIME']), axis = 1)

    # Create new column for mod temp using lambda on row and datetime
    df_combi['MOD_TEMP'] = df_combi.apply(lambda row: return_mod_temp(weather_df, row['DATE_TIME']), axis = 1)

    # Create new column for irradiation using lambda on row and datetime
    df_combi['IRRADIATION'] = df_combi.apply(lambda row: return_irradiation(weather_df, row['DATE_TIME']), axis = 1)

    # Return dataframe
    return df_combi

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
    df_combi['MOD_TEMP'] = df_combi.apply(lambda row: return_mod_temp(weather_df, row['DATE_TIME']), axis = 1)

    # Create new column for irradiation using lambda on row and datetime
    df_combi['IRRADIATION'] = df_combi.apply(lambda row: return_irradiation(weather_df, row['DATE_TIME']), axis = 1)

    # Return dataframe
    return df_combi