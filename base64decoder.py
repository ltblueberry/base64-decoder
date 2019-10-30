#!/usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(
    description='Decode base64 from input file to output file.')

parser.add_argument('-i', '--input', metavar='', help='input file with base64')
parser.add_argument('-o', '--output', metavar='', help='result output file')

args = parser.parse_args()

inputFile = args.input
outputFile = args.output

file = open(inputFile, "r")
base64 = file.read()

result = open(outputFile, "wb")
result.write(base64.decode('base64'))
result.close()


class printColor:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


print "base64 was " + printColor.GREEN + "successfully" + printColor.END + \
    " decoded to " + printColor.BLUE + \
    "{}".format(os.path.abspath(outputFile)) + printColor.END
