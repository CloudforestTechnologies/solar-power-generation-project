'''
kaggle api helper

Providers helper methods for downloading and working with kaggle datasets via api. 
'''

# Module importations (A - Z)
from kaggle.api.kaggle_api_extended import kaggleAPI

# Constants

def retrieve_kaggle_dataset(dataset_url):
    """Retrieve Kaggle Dataset
    ======================================
    Returns a dataset from kaggle using specified url.
    
    Args:
        dataset_url (str) - Url for dataset.
        is_zip (bool) - Indicates whether dataset is returned as zip (will unzip).
        
    Returns:
        dataset (var) - Dataset downloaded from kaggle site.
    """
    
    # Authenticate API
    kaggle_api = kaggle_API()
    kaggle_api.Authenticate()

    # Download dataset
    dataset = kaggle_api.dataset_download_files(dataset_url)
    
    # Return dataset
    return dataset  