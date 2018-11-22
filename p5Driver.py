#! /usr/bin/python

import sys
import os
import re
import pprint
from p5Dict import declareVar, printLabels, printVariables

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
        print('arguments expected : %d, arguments given: %d' %(NUM_ARGS, len(sys.argv)))

        sys.exit(1)

    # get the file name
    filename = sys.argv[1]

    if os.path.isfile(filename) == False:

        print("%s is not a file" %(filename))

        sys.exit(1)

   # compile the regular expressions
    labelRE = re.compile(r'\s*(\w+):')
    varRE   = re.compile(r'^VAR\s([a-zA-Z]+)\s([a-zA-Z]+)\s"?(.*?)"?$')

    # parse the file, store labels and variables
    file = open(filename, 'r')

    print("BEEP source code in %s:"%(filename))

    while True:

        line = file.readline()

        if line == "":
            break

        labelMO = labelRE.match(line) 

        if labelMO != None:

            label = labelMO.group(1).upper()

            value = labelD.get(label, None)

            if value != None:
                print("***Error: label %s appears on multiple lines: %d and %d" %(label, labelD[label], lineNum) )

            else:
                 labelD[label] = lineNum

        else:
            
            varMO = varRE.match(line)

            if varMO != None:
                declareVar(varMO, varTypeD, varValueD)

        fileL.append(line)

        # print line and line number
        print(lineNum, line)

        lineNum += 1

    # print labels and variables

    printVariables(varTypeD, varValueD)

    printLabels(labelD)

main()

        



    



    