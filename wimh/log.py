""" This module log.py is  for logging files scanned """


import  os.path 
import  vars
import  os  
import shutil
import  config

DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_OLD = "old"
DEFAULT_FULL_LOG_DIR = os.path.join(config.DEFAULT_CONFIG_WIMH_FULLPATH, DEFAULT_LOG_DIR) 
DEFAULT_FULL_OLD_DIR = os.path.join(DEFAULT_FULL_LOG_DIR, DEFAULT_LOG_OLD)


def create_logs_dir():
        """ 
            Creaetes the logs directory
            It uses the global constant DEFAULT_FULL_LOG_DIR and DEFAULT_LOG_DIR 
        """

        global DEFAULT_LOG_DIR
        if not os.path.exists(DEFAULT_FULL_LOG_DIR):
            os.makedirs(DEFAULT_FULL_LOG_DIR, vars.file_mode, exist_ok = True) 

def create_old_dir():
        """
            Create  old directory to keep the old logs
        """

        global DEFAULT_FULL_OLD_DIR
        
        if not os.path.exists(DEFAULT_FULL_OLD_DIR):
            os.mkdir(DEFAULT_FULL_OLD_DIR)

def move_log_to_old():
        """ 
            Move old log files to the old directory 
        """ 
       
        global DEFAULT_FULL_LOG_DIR

        
        files = [f for f in os.listdir(DEFAULT_FULL_LOG_DIR) if os.path.isfile(os.path.join(DEFAULT_FULL_LOG_DIR,f))]
        for f in files:
            source = os.path.join(DEFAULT_FULL_LOG_DIR, f)
            destination = os.path.join(DEFAULT_FULL_OLD_DIR, f)
            shutil.move(source, destination)
       
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

def log_audios(relative_path):
        """ 
            Logs the audio files information
            It use the relative path 
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.audio:
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

def log_java_src(relative_path):
        """
            Logs the java source information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.java_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 

def log_java_class(relative_path):
        """
            Logs the java class information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.java_class:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 

def log_java_archive(relative_path):
        """
            Logs the java archive information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.java_archive:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 

def log_java_native_interface(relative_path):
        """
            Logs the java native interface information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.java_native_interface:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close() 

def log_css(relative_path):
        """
            Logs the css information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.css_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()

def log_python_src(relative_path):
        """
            Logs the python source information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.python_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()

def log_python_bytecode(relative_path):
        """
            Logs the python bytecode information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.python_bytecode:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()

def log_go_src(relative_path):
        """
            Logs go source information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.go_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()

def log_html_src(relative_path):
        """
            Logs htm(l) source information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.html_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()

def log_xml_src(relative_path):
        """
            Logs xml source information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.xml_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()

def log_javascript_src(relative_path):
        """
            Logs javascript source information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.javascript_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()

def log_php_src(relative_path):
        """
            Logs php source information
            It use the relative path
        """
        
        #get the absolute path 
        global DEFAULT_FULL_LOG_DIR
       
        absolute_path = os.path.join(DEFAULT_FULL_LOG_DIR, relative_path)
        with open(absolute_path, "w") as fp:
            for entry in vars.php_src:
                fp.write(entry.path)
                fp.write('\n')
        
        fp.close()
