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
                vars.option_numberofdirectories = True
            if args.files:
                vars.option_numberoffiles = True
            if args.symlinks:
                vars.option_numberofsyslinks = True
            if args.c_src_files:
                vars.option_c_src = True
            if args.c_header_files:
                vars.option_c_header = True
    

    #Create the config directory and log directories
    config.create_config_dir()
    log.create_logs_dir()

    #Scan your files/directories and get all the info
    myfile.scan_file_directory(env.get_home_dir())

    #print report 
    report.print_file_info()    

    #log paths
    log.log_directories("dirs")
    log.log_empty_dirs("empty_dirs")
    log.log_files("files")
    log.log_images("images")
    log.log_videos("videos")
    log.log_c_src("c_src_files")
    log.log_c_header("c_header_files")
     

if __name__ == "__main__":
    main()
