""" This is a module for gloabal variables """

file_mode = 0o700

#options 
option_all      = False
option_images   = False
option_videos   = False
option_audios   = False
option_dotfiles = False
option_dotdirectories = False
option_directories = False
option_files = False
option_syslinks = False
option_emptydirs = False
option_c_src = False
option_c_header = False
option_c_plus_src = False
option_c_plus_header = False
option_java_src = False
option_java_class = False
option_java_archive = False
option_java_native_interface = False
option_css = False
option_python_src = False
option_python_bytecode = False
option_go_src = False
option_html_src = False
option_xml_src = False
option_javascript_src = False
option_php_src = False

image_extension =  (
    ".tiff",
    ".jpeg",
    ".gif",
    ".png",
    ".eps",   
    ".raw",
    ".cr2",   
    ".net",   
    ".orf",   
    ".sr2",   
    ".svg",   
    ".webp",
    ".ico"  
)

video_extension = (
    ".avi",  
    ".flv", 
    ".h264",
    ".m4v", 
    ".mkv", 
    ".mov", 
    ".mp3", 
    ".mp4", 
    ".mpg", 
    ".mpeg",
    ".rm" ,
    ".swf", 
    ".vob", 
    ".webm",
    ".wmv", 
)

audio_extension = (
    ".3gp",
    ".aa",
    ".aac",
    ".aax",
    ".act",
    ".aiff",
    ".alac",
    ".amr",
    ".ape",
    ".au",
    ".awb",
    ".dss",
    ".dvf",
    ".flac",
    ".gsm",
    ".iklax",
    ".ivs",
    ".m4a",
    ".m4b",
    ".m4p",
    ".mmf",
    ".mp3",
    ".mpc",
    ".msv",
    ".ogg",
    ".oga",
    ".mogg",
    ".opus",
    ".ra",
    ".rm",
    ".raw",
    ".rf64",
    "sln",
    "tta",
    ".voc",
    ".vox",
    ".wav",
    ".wma",
    ".wv",
    ".webm",
    ".8svc",
    ".cda"
) 

#list of file object  to collect 
directories = []
files = []
symbolic_links = []
empty_dirs = []
images = []
videos = []
audio  = []

dot_directories = []
dot_files = []


#programming files

#c/c files
c_src = []              #.c
c_header = []           #.h
c_plus_src = []         #.cc
c_plus_header = []      #.hh

css_src = []

java_src = []           #.java
java_class = []         #.class
java_archive = []       #.jar
java_native_interface = [] #.jni

#python
python_src = []         #.py
python_bytecode = []    #.pyc

#golang
go_src = []             #.go

#html_src
html_src = []           #.html or htm or xhtml

#xml source
xml_src = []            #.xml


#javascript
javascript_src = []     #.js

#php
php_src = []            #.php


#perl
perl_serc = []          #.pl or .PL

#visual basic
visual_basic_project = []    #.vbp
visual_basic_form_module = [] #.frm
visual_basic_standard_code_module = [] #.bas
visual_basic_custom_controls = [] #.ocx
visual_basic_project_form = [] #.vbw


class sourceCode_info:
    def __init__(self): 
        self.c_src = 0 
        self.c_header = 0
        self.cplus_src = 0
        self.cplus_header = 0
        self.css_src = 0
        self.java_src = 0
        self.python_src = 0
        self.go_src = 0
        self.html_src = 0
        self.xhtml_src = 0
        self.javascript_src = 0
        self.php_src = 0  
        self.perl_src = 0
        self.vb_src = 0
    def c_src_add(self):
        self.c_src += 1 
    def c_header_add(self):
        self.c_header += 1
    def cplus_src_add(self):
        self.cplus_src += 1
    def css_src_add(self):
        self.css_src += 1
    def java_src_add(self):
        self.java_src += 1
    def python_src_add(self):
        self.python_src += 1
    def go_src_add(self):
        self.go_src += 1
    def html_src_add(self):
        self.html_src += 1
    def xhtml_add(self):
        self.xhtml_src += 1
    def javascript_src_add(self):
        self.javascript_src +=1 
    def php_src_add(self):
        self.php_src += 1
    def perl_src_add(self):
        self.perl_src += 1
    def vb_src_add(self):
        self.vb_src += 1
    def print_info(self):
        print("C Source code: ", self.c_src)
        print("C Header code: ", self.c_header)
        print("C++ Source code: ", self.cplus_src) 
        print("C++ Header code: ",self.cplus_header)
        print("Css Source code: ",self.css_src)
        print("Java Source code: ",self.java_src)
        print("Python Souce code: ",self.python_src)
        print(self.go_src)
        print(self.html_src)
        print(self.xhtml_src)
        print(self.javascript_src)
        print(self.php_src)  
        print(self.perl_src)
        print(self.vb_src)
