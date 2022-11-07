""" This is configuration module """

import os
import vars
import env

#default config variables constants 
DEFAULT_CONFIG_DIR = ".config"
DEFAULT_CONFIG_WIMH = "wimh"
DEFAULT_CONFIG_WIMH_FULLPATH = os.path.join(env.get_home_dir()  , DEFAULT_CONFIG_DIR, DEFAULT_CONFIG_WIMH)

def create_config_dir():
    """ 
    This function creates a config directory 
    It uses global constant DEFAULT_CONFIG_WIMH_FULLPATH 
    """

    if not os.path.exists(DEFAULT_CONFIG_WIMH_FULLPATH):
        os.makedirs(DEFAULT_CONFIG_WIMH_FULLPATH, vars.file_mode, exist_ok = True) 
