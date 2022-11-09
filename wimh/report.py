'''This is a module for outputing information'''

import vars
def print_file_info():
    ''' This is out of file information '''

    if vars.option_all == True:
        print(f"Number of Directories: {len(vars.directories)} ");
        print(f"Number of Files {len(vars.files)}")
        print(f"Number of Symbolic links {len(vars.symbolic_links)} ")
        print(f"Number of Empty directories {len(vars.empty_dirs)} ")
        print(f"Number of Images {len(vars.images)} ")
        print(f"Number of Videos {len(vars.videos)} ")
        print(f"Number of Audios {len(vars.audio)} ")
        print(f"Number of Dot Files {len(vars.dot_files)} ")
        print(f"Number of Dot Directories {len(vars.dot_directories)} ")
        print(f"Number of C source files {len(vars.c_src)} ")
        print(f"Number of C header files {len(vars.c_header)} ")
        print(f"Number of C++ source files {len(vars.c_plus_src)} ")
        print(f"Number of C++ header files {len(vars.c_plus_header)} ")
        print(f"Number of Java source files {len(vars.java_src)} ")
        print(f"Number of Java class files {len(vars.java_class)} ")
        print(f"Number of Java archive  files {len(vars.java_archive)} ")
        print(f"Number of Java native interface files {len(vars.java_native_interface)} ")

    else:
            if vars.option_numberofdirectories == True:
                     print(f"Number of Directories: {len(vars.directories)} ");
            if vars.option_numberoffiles == True:
                    print(f"Number of Files {len(vars.files)}")
            if vars.option_numberofsyslinks == True:
                    print(f"Number of Symbolic links {len(vars.symbolic_links)} ")
            if vars.option_emptydirs == True:
                    print(f"Number of Empty directories {len(vars.empty_dirs)} ")
            if vars.option_images == True:
                    print(f"Number of Images {len(vars.images)} ")
            if vars.option_videos == True:
                    print(f"Number of Videos {len(vars.videos)} ")
            if vars.option_audios == True:
                    print(f"Number of Audios {len(vars.audio)} ")
            if vars.option_dotfiles == True:
                    print(f"Number of Dot Files {len(vars.dot_files)} ")
            if vars.option_dotdirectories == True:
                    print(f"Number of Dot Directories {len(vars.dot_directories)} ")
            if vars.option_c_src == True:
                    print(f"Number of C Source files {len(vars.c_src)} ")
            if vars.option_c_header == True:
                    print(f"Number of C Header files {len(vars.c_header)} ")
            if vars.option_c_plus_src == True:
                    print(f"Number of C++ Source files {len(vars.c_plus_src)} ")
            if vars.option_c_plus_header == True:
                    print(f"Number of C++ header files {len(vars.c_plus_header)} ")
            if vars.option_java_src == True:
                    print(f"Number of Java source files {len(vars.java_src)} ")
            if vars.option_java_class == True:
                    print(f"Number of Java class files {len(vars.java_class)} ")
            if vars.option_java_archive == True:
                    print(f"Number of Java archive files {len(vars.java_archive)} ")
            if vars.option_java_native_interface == True:
                    print(f"Number of Java java native interface files {len(vars.java_native_interface)} ")

