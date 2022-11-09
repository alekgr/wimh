""" This is the myfile module where all the magic happens """

import os
import magic
import vars

def getFileExtention(filepath):
    """ Return the file extension """

    return os.path.splitext(filepath)[-1]

def get_file_pre(filepath):
    """ Return file base """

    return os.path.basename(filepath)[0]


def is_empty_directory(path):
    """ Check if directory is empty """

    items = os.listdir(path)
    if len(items) == 0:
        return True    
    else:
        return False  

def scan_file_directory(path):
    """
        Scan files and  directories  and increment counter for each
    """

    items = os.scandir(path)
    for entry in items:
        if entry.is_dir():
            if is_empty_directory(entry.path) == True:
                vars.empty_dirs.append(entry)    
            vars.directories.append(entry)
            if is_dot(entry.path):
                vars.dot_directories.append(entry)
            scan_file_directory(entry.path)
        if entry.is_file():
            vars.files.append(entry)
            process_file(entry) 

        if entry.is_symlink():
            vars.symbolic_links.append(entry)

       
def get_category(ext):
    """ Return category of the file by and extension """

    if ext in vars.image_extension: 
        return "image"
    if ext in vars.video_extension:
        return "video"
    if ext in vars.audio_extension:
        return "audio"

def printDirectories():
    """ Print all directories paths """
        
    for i in vars.directories:
        print(i.path)

def printEmptydirectories():
    """ Print empty directories """

    for entry in vars.empty_dirs:
        print(entry)

def printFiletypes():
    """ print file types """

    for entry in vars.files:
        type = magic.from_file(entry.path)
        print(type)

def isImage(path):
    """ Check if file path is an image """

    if getFileExtention(path) in vars.image_extension:
        return True

def isVideo(path):
    """ Check if file path is a video """

    if getFileExtention(path) in vars.video_extension: 
        return True

def isAudio(path):
    """ Check if file path is a audio """

    if getFileExtention(path) in vars.audio_extension:
        return True

def is_dot(path):
    """ Checks if file path(both directory and file) if it is a dot file """

    if get_file_pre(path) == '.':
        return True

def is_c_src(path):
    """ Checks if path file is a c source file """

    if getFileExtention(path) == ".c":
        return True    

def is_c_header(path):
    """ Checks if path file is a c header file """

    if getFileExtention(path) == ".h":
        return True

def is_c_plus_src(path):
    """ Checks if path file is a c++ source file """

    if getFileExtention(path) ==  ".cc":
        return True

def is_c_plus_header(path):
    """ Checks if path file is a c++ header files """

    if getFileExtention(path) == ".hh":
        return True

def is_java_src(path):
    """ Checks if path file is a .java source files """

    if getFileExtention(path) == ".java":
        return True

def is_java_class(path):
    """ Checks if path file is a java .class files """

    if getFileExtention(path) == ".class":
        return True

def is_java_archive(path):
    """ Checks if path file is .jar Java archive files """

    if getFileExtention(path) == ".jar":
        return True

def  is_java_native_interface(path):
    """ checks if path file is a .jni Java native interface file """

    if getFileExtention(path) == ".jni":
        return True

def  is_css(path):
    """ Checks if path file is a .css file"""

    if getFileExtention(path) == ".css":
        return True

def is_python_src(path):
    """ Checks if path file is a .py file """

    if getFileExtention(path) == ".py":
        return True

def is_python_bytecode(path): 
    """ Checks if path files  is .pyc file """

    if getFileExtention(path) == ".pyc":
        return True

def is_go_src(path):
    """ Checks if path file is .go golang file """

    if getFileExtention(path) == ".go":
        return True

def is_html_src(path):
    """ Checks if path file is .htm(l) file or xhtml """

    if getFileExtention(path) == ".html" or getFileExtention(path) == ".htm" or getFileExtention(path) == ".xhtml":
        return True

def is_xml_src(path):
    """ Checks if path file is a .xml file """

    if getFileExtention(path) == ".xml":
        return True    

def is_javascript_src(path):
    """ Checks if path file is javascript file """

    if getFileExtention(path) == ".js":
        return True

def process_file(entry):
    """ Process action for file type """

    if isImage(entry.path):
        vars.images.append(entry)
    elif isVideo(entry.path):
        vars.videos.append(entry)
    elif isAudio(entry.path):
        vars.audio.append(entry)
    elif is_dot(entry.path):
        vars.dot_files.append(entry)
    elif is_c_src(entry.path):
        vars.c_src.append(entry)
    elif is_c_header(entry.path):
        vars.c_header.append(entry)
    elif is_c_plus_src(entry.path):
        vars.c_plus_src.append(entry)
    elif is_c_plus_header(entry.path):
        vars.c_plus_header.append(entry)
    elif is_java_src(entry.path):
        vars.java_src.append(entry)
    elif is_java_class(entry.path):
        vars.java_class.append(entry)
    elif is_java_archive(entry.path):
        vars.java_archive.append(entry)
    elif is_java_native_interface(entry.path):
        vars.java_native_interface.append(entry)
    elif is_css(entry.path):
        vars.css_src.append(entry)
    elif is_python_src(entry.path):
        vars.python_src.append(entry)
    elif is_python_bytecode(entry.path):
        vars.python_bytecode.append(entry)
    elif is_go_src(entry.path):
        vars.go_src.append(entry)
    elif is_html_src(entry.path):
        vars.html_src.append(entry)
    elif is_xml_src(entry.path):
        vars.xml_src.append(entry)
    elif is_javascript_src(entry.path):
        vars.javascript_src.append(entry)
