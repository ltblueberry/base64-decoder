#!/usr/bin/python

import argparse
import os
import sys


class printColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


parser = argparse.ArgumentParser(
    description='Decode base64 from input file to output file.')

parser.add_argument('-i', '--input', metavar='',
                    help='input file path with base64')
parser.add_argument('-o', '--output', metavar='', help='output file path')

args = parser.parse_args()

inputFile = args.input
outputFile = args.output

if inputFile is None:
    print "-i, --input" + printColor.RED + \
        "     input file path is not defined" + printColor.END
    sys.exit(1)

if outputFile is None:
    print "-o, --output" + printColor.RED + \
        "     output file path is not defined" + printColor.END
    sys.exit(1)

if os.path.exists(inputFile) == False:
    print printColor.RED + \
        "File {} was not found".format(
            os.path.abspath(inputFile)) + printColor.END
    sys.exit(1)

file = open(inputFile, "r")
base64 = file.read()

result = open(outputFile, "wb")
result.write(base64.decode('base64'))
result.close()


print "base64 was " + printColor.GREEN + "successfully" + printColor.END + \
    " decoded to " + printColor.BLUE + \
    "{}".format(os.path.abspath(outputFile)) + printColor.END

sys.exit(0)
