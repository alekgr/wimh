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
