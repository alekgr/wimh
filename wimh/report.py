'''This is a module for outputing information'''

import vars
def print_file_info():
    ''' This is out of file information '''

    BOLD = '\033[1m'
    END  = '\033[0m'

    if vars.option_all == True:
        print(BOLD + "General file Information *******" + END)
        print(f"\tNumber of Directories: {len(vars.directories)} ");
        print(f"\tNumber of Files {len(vars.files)}")
        print(f"\tNumber of Symbolic links {len(vars.symbolic_links)} ")
        print(f"\tNumber of Empty directories {len(vars.empty_dirs)} ")
        print(f"\tNumber of Dot Files {len(vars.dot_files)} ")
        print(f"\tNumber of Dot Directories {len(vars.dot_directories)} ")

        print(BOLD + "Media *******" + END)
        print(f"\tNumber of Images {len(vars.images)} ")
        print(f"\tNumber of Videos {len(vars.videos)} ")
        print(f"\tNumber of Audios {len(vars.audio)} ")
        print(BOLD + "Project Source code *******" + END)
        print(f"\tNumber of C source files {len(vars.c_src)} ")
        print(f"\tNumber of C header files {len(vars.c_header)} ")
        print(f"\tNumber of C++ source files {len(vars.c_plus_src)} ")
        print(f"\tNumber of C++ header files {len(vars.c_plus_header)} ")
        print(f"\tNumber of Java source files {len(vars.java_src)} ")
        print(f"\tNumber of Java class files {len(vars.java_class)} ")
        print(f"\tNumber of Java archive  files {len(vars.java_archive)} ")
        print(f"\tNumber of Java native interface files {len(vars.java_native_interface)} ")
        print(f"\tNumber of css files {len(vars.css_src)} ")
        print(f"\tNumber of python source files {len(vars.python_src)} ")
        print(f"\tNumber of python bytecode files {len(vars.python_bytecode)} ")
        print(f"\tNumber of go source files {len(vars.go_src)} ")
        print(f"\tNumber of htm(l) source files {len(vars.html_src)} ")
        print(f"\tNumber of xml source files {len(vars.xml_src)} ")
        print(f"\tNumber of javascript source files {len(vars.javascript_src)} ")
        print(f"\tNumber of php source files {len(vars.php_src)} ")

    else:
            if vars.option_directories == True:
                     print(f"Number of Directories: {len(vars.directories)} ");
            if vars.option_files == True:
                    print(f"Number of Files {len(vars.files)}")
            if vars.option_syslinks == True:
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
            if vars.option_css == True:
                    print(f"Number of css files {len(vars.css_src)} ")
            if vars.option_python_src == True:
                    print(f"Number of python source files {len(vars.python_src)} ")
            if vars.option_python_bytecode == True:
                    print(f"Number of python bytecode {len(vars.python_bytecode)} ")
            if vars.option_go_src == True:
                    print(f"Number of go source files {len(vars.go_src)} ")
            if vars.option_html_src == True:
                    print(f"Number of htm(l) source files {len(vars.html_src)} ")
            if vars.option_xml_src == True:
                    print(f"Number of xml source files {len(vars.xml_src)} ")
            if vars.option_javascript_src == True:
                    print(f"Number of javascript files {len(vars.javascript_src)} ")
            if vars.option_php_src == True:
                    print(f"Number of php source files {len(vars.php_src)} ")
