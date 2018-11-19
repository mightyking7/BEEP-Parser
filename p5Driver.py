#! /usr/bin/python

import sys
import sys.os
import re
from p5Dict import declareVar

def main():

    NUM_ARGS = 2

    if len(sys.argv) < NUM_ARGS:

        print("filename needed as command argmuent")

        sys.exit(1)

    elif len(sys.argv) > NUM_ARGS:

        #TODO use formated printing
        print('arguments expected : ' + NUM_ARGS + ', arguments given: ' + len(sys.argv))

        sys.exit(1)

    # get the file name
    filename = argv[1]

    if os.path.isfile(filename) == False:

        print( filename + " is not a file")

        sys.exit(1)

   # compile the regular
    labelRE = re.compile(r'^([a-z]+):')
    varRE   = re.compile(r'^VAR\s[a-z]+\s([a-z]+)\s([\'"\w]*)')

    # parse the file and store labels and variables
    file = open(filename, 'r')

    fileStr = file.read()

    for num, line in enumerate(fileStr, 1):

        labelMO = labelRE.match(line) 

        if labelMO != None:

            label = labelMO.group(1)

            labelD[num] = label.upper()

        elif varMO = varRE.match(line) != None:

            var = varMO.group(1)

            varTypeD[]

        else:




        


        


'''
Prints the formated string with the specified arguments and exits the program
'''
#def errExit(format, * args):

        



    



    