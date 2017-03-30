import sys
import os.path
import datetime
import getopt
import argparse
from shutil import copyfile

#### create directory for test data ####
def dir():
    global parentdir
    parentdir = os.path.dirname(os.path.abspath(__file__))
    try:
        if namespace.pathdir is not None:
            namespace.pathdir=os.path.normpath(namespace.pathdir)
            if os.path.exists(namespace.pathdir)== False:
                os.mkdir(namespace.pathdir)
                print "Directory '", namespace.pathdir, "' will be used to save test data"
        else:
            namespace.pathdir=parentdir
            print "Current directory: '", namespace.pathdir, "' will be used to save test data"
    except:
        print "Error! Can't create directory"

#### create source file for duplicates ####
def fil():
    try:
        if namespace.sourcefile is not None:
            namespace.sourcefile=os.path.normpath(namespace.sourcefile)
            if os.path.exists(namespace.sourcefile)== False:
                file = open(namespace.sourcefile, "w")
                file.close()
            else:
                print "Error! File '", namespace.sourcefile, "' exists"
                sys.exit(1)
        else:
            currenttime=datetime.datetime.now().strftime('%d.%m.%Y-%H.%M.%S.')
            filename = "file"+currenttime+"txt"
            namespace.sourcefile=os.path.normpath(parentdir+"/"+filename)
            file = open(namespace.sourcefile, "w")
            file.close()
            print "Created file: '", namespace.sourcefile, "' will be used to create duplicates"
    except:
        print "Error! Can't create file"

#### create duplicates ####
def duplicates():
    i=1
    while i <= namespace.duplicatesnumber:
        duplicatefile = os.path.normpath(namespace.pathdir + "/Duplicate" + str(i))
        copyfile(namespace.sourcefile, duplicatefile)
        print "Created duplicate file: '", duplicatefile, "'"
        i += 1

#### change modification date of duplicate ####
def modificationdate():
    files = os.listdir(namespace.pathdir)
    if files:
        files = [os.path.join(namespace.pathdir, file) for file in files]
        files = [file for file in files if os.path.isfile(file)]
    last_modified_date = max(files, key=os.path.getmtime)
    file = open(last_modified_date, "w")
    file.close()
    print "File: '", last_modified_date, "' was modified. File has a last modification date"

#### create parser for input values ####
def createparser ():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument ('-d', '--pathdir', action='store', dest='pathdir', help='Set path to directory for test data')
        parser.add_argument ('-n', '--duplicatesnumber', action='store', dest='duplicatesnumber', help='Set number of duplicates', type=int, default=5)
        parser.add_argument ('-f', '--sourcefile', action='store', dest='sourcefile', help='Set path to source file for creating of duplicates')
        return parser
    except getopt.GetoptError:
        sys.exit(1)

if __name__ == '__main__':
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])
    dir()
    fil()
    duplicates()
    modificationdate()