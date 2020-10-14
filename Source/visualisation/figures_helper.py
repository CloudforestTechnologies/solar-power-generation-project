'''
figures_helper

This file supports operations on figures, such as saving files.
'''

# Module Importations
from datetime import datetime

TITLE_FONTSIZE = 18
PROJECT_CODE = 'WJ'
SAVE_FORMAT = '.png'
SAVE_DPI = 600

# Helper Method for saving figures
def generate_fig_save_string(filename):
    """Save Figures
    ======================================
    Saves figures using prescribed filename, date/timestamp and directory.
    
    Args:
        filename (string) - Filename to be used for figure.
        
    Returns:
        save_string (string) - String to use for saving file.
    """

    # Save files to project
    filedirectory = r'C:/Developer/solar-power-generation-project/Reports/Figures'

    # Retrieve timestamp
    timestamp = datetime.now()
    timestamp_str = timestamp.strftime('%Y_%m_%d-%H_%M_%S')

    # Create filepath
    filepath = filedirectory + '/' + PROJECT_CODE + '_' + filename + '_' + timestamp_str + SAVE_FORMAT

    # Return save string
    return filepath