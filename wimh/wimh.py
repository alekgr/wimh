#!/usr/bin/env python3

""" wimh.py program  """

#import magic
import sys
import argparse
import myfile
import report
import log
import vars
import config
import env

def main():

    #Get options
    parser = argparse.ArgumentParser(
            prog="wimh",
            description="Command line file parser",
            #formatter_class=argparse.RawTextHelpFormatter
    )


    #add arguemnt for --all
    parser.add_argument('--all', action='store_true', help="Report everything")
    #add argument for --images
    parser.add_argument('--images', action='store_true', help="Report number of images")
    #add argument for --videos
    parser.add_argument('--videos', action='store_true', help="Report number of  videos")
    #add arguemnt for --audios
    parser.add_argument('--audios', action='store_true', help="Report number of  audios")
    #add arguemnt for --dotfiles
    parser.add_argument('--dotfiles', action='store_true', help="Report number of  dotfiles")
    #add argument for --dotdirectories 
    parser.add_argument('--dotdirs', action='store_true', help="Report number of  dot directories")
    #add argument for --dirs
    parser.add_argument('--dirs', action='store_true', help="Report number of  directories")
    #add argument for --files
    parser.add_argument('--files', action='store_true', help="Report number of  files")
    #add arguemtn for --symlinks
    parser.add_argument('--symlinks', action='store_true', help="Report number of symlinks")
    #add argument for --emptydirs
    parser.add_argument('--emptydirs', action='store_true', help="Report number of emptydirs")
    #add argument for --c_src_files
    parser.add_argument('--c_src_files', action='store_true', help="Report number of C source files")
    #add argument for --c_header_files
    parser.add_argument('--c_header_files', action='store_true', help="Report number of C header files")
    #add argument for --cplus_src_files
    parser.add_argument('--cplus_src_files', action='store_true', help="Report number of C++ source files")
    #add argument for --cplus_header_files
    parser.add_argument('--cplus_header_files', action='store_true', help="Report number of C++ header files")
    #add argument for --java_src_files
    parser.add_argument('--java_src_files', action='store_true', help="Report number of Java source files")
    #add argument for --java_class
    parser.add_argument('--java_class_files', action='store_true', help="Report number of Java  class files")
    #add argument for --java_archive
    parser.add_argument('--java_archive_files', action='store_true', help="Report number of Java archive files")
    #add argument for --java_native_interface
    parser.add_argument('--java_native_interface_files', action='store_true', help="Report number of Java native interface files")
    #add arguemnt for --css
    parser.add_argument('--css', action='store_true', help="Report number of css files")
    #add argument for --python_src
    parser.add_argument('--python_src', action='store_true', help="Report number of python source files")
    #add argument for --python_bytecode
    parser.add_argument('--python_bytecode', action='store_true', help="Report number of python bytecode files")
    #add argument for --go_src
    parser.add_argument('--go_src', action='store_true', help="Report number of go source files")
    #add argument for --html_src
    parser.add_argument('--html_src', action='store_true', help="Report number of htm(l) source  files")
    #add argument for --xml_src
    parser.add_argument('--xml_src', action='store_true', help="Report number of xml source files")
    #add argument for --javascript_src
    parser.add_argument('--javascript_src', action='store_true', help="Report number of javascript source files")
    #add argument for --php_src
    parser.add_argument('--php_src', action='store_true', help="Report number of php source files")

    
    #setup parsers variables 
    args = parser.parse_args()
    if len(sys.argv) == 1:
       vars.option_all = True 
    else:
        #set options
        if  args.all:
            vars.option_all = True
        else:
            if args.images:
                vars.option_images = True
            if args.videos:
                vars.option_videos = True
            if args.audios:
                vars.option_audios = True
            if args.dotfiles:
                vars.option_dotfiles = True
            if args.dotdirs:
                vars.option_dotdirectories = True
            if args.dirs:
                vars.option_directories = True
            if args.files:
                vars.option_files = True
            if args.symlinks:
                vars.option_syslinks = True
            if args.emptydirs:
                vars.option_emptydirs = True
            if args.c_src_files:
                vars.option_c_src = True
            if args.c_header_files:
                vars.option_c_header = True
            if args.cplus_src_files:
                vars.option_c_plus_src = True
            if args.cplus_header_files:
                vars.option_c_plus_header = True
            if args.java_src_files:
                vars.option_java_src = True
            if args.java_class_files:
                vars.option_java_class = True
            if args.java_archive_files:
                vars.option_java_archive = True
            if args.java_native_interface_files:
                vars.option_java_native_interface = True
            if args.css:
                vars.option_css = True
            if args.python_src:
                vars.option_python_src = True
            if args.python_bytecode:
                vars.option_python_bytecode = True
            if args.go_src:
                vars.option_go_src = True
            if args.html_src:
                vars.option_html_src = True
            if args.xml_src:
                vars.option_xml_src = True
            if args.javascript_src:
                vars.option_javascript_src = True
            if args.php_src:
                vars.option_php_src = True


    #Create the config directory and log directories
    config.create_config_dir()
    log.create_logs_dir()

    #Scan your files/directories and get all the info
    myfile.scan_file_directory(env.get_home_dir())

    #print report 
    report.print_file_info()    

    #log paths
    log.create_logs_dir()
    log.move_log_to_old()

    if vars.option_directories == True or vars.option_all == True:
        log.log_directories("dirs") 
    if vars.option_emptydirs == True or vars.option_all == True:
        log.log_empty_dirs("empty_dirs")
    if vars.option_files == True or vars.option_all == True:
        log.log_files("files")
    if vars.option_images == True or vars.option_all == True:
        log.log_images("images")
    if vars.option_audios == True or vars.option_all == True:
        log.log_audios("audios")
    if vars.option_videos == True or vars.option_all == True:
        log.log_videos("videos")
    if vars.option_c_src == True or vars.option_all == True:
        log.log_c_src("c_src_files")
    if vars.option_c_header == True or vars.option_all == True:
        log.log_c_header("c_header_files")
    if vars.option_c_plus_src == True or vars.option_all == True:
        log.log_c_plus_src("c++_src_files")
    if vars.option_c_plus_header == True or vars.option_all == True:
        log.log_c_plus_header("c++_header_files")
    if vars.option_java_src == True or vars.option_all == True:
        log.log_java_src("Java_source_files")
    if vars.option_java_class == True or vars.option_all == True:
        log.log_java_class("Java_class_files")
    if vars.option_java_archive == True or vars.option_all == True:
        log.log_java_archive("Java_class_archive")
    if vars.option_java_native_interface == True or vars.option_all == True:
        log.log_java_native_interface("Java_native_interface")
    if vars.option_css == True or vars.option_all:
        log.log_css("css")
    if vars.option_python_src == True or vars.option_all == True:
        log.log_python_src("Python_src")
    if vars.option_python_bytecode == True or  vars.option_all == True:
        log.log_python_bytecode("Python_bytecode")
    if vars.option_go_src == True or vars.option_all == True:
        log.log_go_src("go_src")
    if vars.option_html_src == True or vars.option_all == True:
        log.log_html_src("html_src")
    if vars.option_xml_src == True or vars.option_all == True:
        log.log_xml_src("xml_src")
    if vars.option_javascript_src or vars.option_all == True:
        log.log_javascript_src("javascript_src")
    if vars.option_php_src == True or vars.option_all == True:
        log.log_php_src("php_src")
     

if __name__ == "__main__":
    main()
