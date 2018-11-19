#! /usr/bin/python

import sys
import sys.os

def main():

    NUM_ARGS = 2

    if len(sys.argv) < NUM_ARGS:

        print("filename needed as command argmuent")

        sys.exit(1)

    elif len(sys.argv) > NUM_ARGS:

        #TODO use formated printing
        print('arguments expected : ' + NUM_ARGS + ', arguments given: ' + len(sys.argv))

        sys.exit(1)

    filename = argv[1]

    if os.path.isfile(filename) == False:

        print( filename + " is not a file")

        sys.exit(1)

    file = open(filename, 'r')

    while True:

        line = file.readline()

        # check for EOF
        if line == "":
            break
        
        

        


'''
Prints the formated string with the specified arguments and exits the program
'''
#def errExit(format, * args):

        



    



    