"""
This is the env module for getting enviorment variables
"""

import os

def get_home_dir():
    """ get homr dir """

    return os.getenv("HOME")
    
