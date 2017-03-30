# script-file-duplicate
Created script for creating of file duplicates using Python

Task:
Write a script that can:
- accept the path to the directory as input parameter where the test files will be created data
- if the path to the directory is not specified, than it is equal to the current folder in which the script is executed
- if the specified directory does not exist, then try to create it
- accept the number of duplicates as input parameter
- if this value is not specified, then it equal to 5
- accept the path to the source file as input parameter, which will be the original for creation of duplicates
- if no file path is specified, then create any text file
- create a specified number of duplicates with numbering (Duplicate1, Duplicate2, ...) and save them along the specified path
- change the modification date to any one of the duplicates so that it is newer other duplicates

General stack of technologies: 
- Python

Preconditions:
-	Installed Python 2.7

Instructions:

`usage: script-file-duplicate.py [-h] [-d PATHDIR] [-n DUPLICATESNUMBER]`
`                                [-f SOURCEFILE]                        `

`optional arguments:`

`  -h, --help                                                   show this help message and exit`

`  -d PATHDIR, --pathdir PATHDIR                                Set path to directory for test data`

`  -n DUPLICATESNUMBER, --duplicatesnumber DUPLICATESNUMBER     Set number of duplicates`

`  -f SOURCEFILE, --sourcefile SOURCEFILE                       Set path to source file for creating of duplicates`
