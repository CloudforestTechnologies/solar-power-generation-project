'''
Constants

Provides store of constants for use with this project

'''
# Module Imports
import os

def return_project_code():
    return 'WJ'

def return_model_save_path():
    return r'C:\Developer\solar-power-generation-project\Models'

def return_tensorboard_log_path():

    root = os.getcwd()
    branch = r"Models\TensorBoard"

    path = os.path.join(root, branch)
    
    return path