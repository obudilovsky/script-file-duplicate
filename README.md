# script-file-duplicate
Created script for creating of file duplicates using Python

Task:
Write a script that can:
    - accept the path to the directory where the test files will be created
data;
    - If the path to the directory is not specified, then assume that it is equal to the current folder in which
The script is executed;
    - If the specified directory does not exist, then try to create it.
    - accept the number of duplicates;
    - If this value is not specified, then count it equal to 5;
    - accept the path to the source file, which will be the original for
Creation of duplicates;
    - if no file path is specified, then create any text file;
    - create a specified number of duplicates with their numbering (Duplicate1,
Duplicate2, ...) and save them along the specified path;
    - Change the modification date to any one of the duplicates so that it is newer other duplicates.


General stack of technologies: 
- Python

Preconditions:
-	Installed Python 2.7

Instructions:
usage: script-file-duplicate.py [-h] [-d PATHDIR] [-n DUPLICATESNUMBER]
                                [-f SOURCEFILE]

optional arguments:
  -h, --help            show this help message and exit
  -d PATHDIR, --pathdir PATHDIR
                        Set path to directory for test data
  -n DUPLICATESNUMBER, --duplicatesnumber DUPLICATESNUMBER
                        Set number of duplicates
  -f SOURCEFILE, --sourcefile SOURCEFILE
                        Set path to source file for creating of duplicates
