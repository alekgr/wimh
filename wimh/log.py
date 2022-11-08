""" This module log.py is  for logging files scanned """


import  os.path 
import  vars
import  os  
import  config

DEFAULT_LOG_DIR = "logs"
DEFAULT_FULL_LOG_DIR = os.path.join(config.DEFAULT_CONFIG_WIMH_FULLPATH, DEFAULT_LOG_DIR) 


def create_logs_dir():
        """ 
            Creaetes the logs directory
            It uses the global constant DEFAULT_FULL_LOG_DIR and DEFAULT_LOG_DIR 
        """

        global DEFAULT_LOG_DIR
        if not os.path.exists(DEFAULT_FULL_LOG_DIR):
            os.makedirs(DEFAULT_FULL_LOG_DIR, vars.file_mode, exist_ok = True) 

def log_directories(relative_path):
        """ 
            Logs the direcotiries information 
            It uses the relative path argument 
        """
   
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)

        with open(absolute_path, "w") as fp:
            for entry in vars.directories:
                fp.write(entry.path)
                fp.write('\n')
        fp.close()  

def log_files(relative_path):
        """
            Logs the files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)


        with open(absolute_path, "w") as fp:
            for entry in vars.files:
                fp.write(entry.path)
                fp.write('\n')
        fp.close()  

def log_empty_dirs(relative_path):
        """
            Logs the empty directory information
            It use the relative path 
        """
    
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR

        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.empty_dirs:
                fp.write(entry.path)
                fp.write('\n')
        fp.close()  

def log_images(relative_path):
        """ 
            Logs the image files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.images:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()  

def log_videos(relative_path):
        """ 
            Logs the image files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.videos:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()  

def log_c_src(relative_path):
        """ 
            Logs the c source files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.c_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 

def log_c_header(relative_path):
        """ 
            Logs the c header files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.c_header:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 

def log_c_plus_src(relative_path):
        """ 
            Logs the c++ source files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.c_plus_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 

def log_c_plus_header(relative_path):
        """ 
            Logs the c++ header files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.c_plus_header:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 
