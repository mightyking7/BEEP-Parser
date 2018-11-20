#! /usr/bin/python

import sys
import os
import re

def main():

    varTypeD = {}   # dictionary for var data type

    varValueD = {}  # dictionary for var value

    labelD = {}     # dictionary for labels

    fileL = []      # lines of file stored as entry in list 

    lineNum = 1     # line number in file

    NUM_ARGS = 2    # number of args in command line

    if len(sys.argv) < NUM_ARGS:

        print("filename needed as command argmuent")

        sys.exit(1)

    elif len(sys.argv) > NUM_ARGS:

        #TODO use formated printing
        print('arguments expected : ' + NUM_ARGS + ', arguments given: ' + len(sys.argv))

        sys.exit(1)

    # get the file name
    filename = sys.argv[1]

    if os.path.isfile(filename) == False:

        print( filename + " is not a file")

        sys.exit(1)

   # compile the regular expressions
    labelRE = re.compile(r'^([a-z]+):')
    varRE   = re.compile(r'^VAR\s([a-z]+)\s([a-z]+)\s([\'"\w]*)')

    # parse the file, store labels and variables
    file = open(filename, 'r')

    print("BEEP source code in " + filename + " :")

    while True:

        line = file.readline()

        if line == "":
            break

        labelMO = labelRE.match(line) 

        if labelMO != None:

            label = labelMO.group(1).upper()

            value = labelD.get(label, None)

            if value != None:
                print("***Error: label " + label + " appears on multiple lines: " + labelD[label] + " and " + num)

            else:
                 labelD[label] = lineNum

        else:
            
            varMO = varRE.match(line)

            if varMO != None:
                #declareVar(varMO, varTypeD, varValueD)
                print("Var found")

        fileL.append(line)

        # print line and line number
        print(lineNum, line)

        lineNum += 1

    # print labels and variables
    print(labelD)


'''
Prints the formated string with the specified arguments and exits the program
'''
#def errExit(format, * args):


main()

        



    



    