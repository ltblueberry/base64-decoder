#!/usr/bin/python

import argparse
import os
import sys


class printColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


class messages:
    NONE_INPUT = "input file path is not defined"
    NONE_OUTPUT = "output file path is not defined"
    FILE_NOT_FOUND = "File {} was not found"
    DONE = "done"


need_print = False


def print_if_needed(string):
    if need_print:
        print string


def main(inputFile, outputFile):

    if inputFile is None:
        exit_message = messages.NONE_INPUT
        print_if_needed("-i, --input     " + printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    if outputFile is None:
        exit_message = messages.NONE_OUTPUT
        print_if_needed("-o, --output    " + printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    if os.path.exists(inputFile) == False:
        exit_message = messages.FILE_NOT_FOUND.format(
            os.path.abspath(inputFile))
        print_if_needed(printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    file = open(inputFile, "r")
    base64 = file.read()

    result = open(outputFile, "wb")
    result.write(base64.decode('base64'))
    result.close()

    print_if_needed("base64 was " + printColor.GREEN + "successfully" + printColor.END +
                    " decoded to " + printColor.BLUE +
                    "{}".format(os.path.abspath(outputFile)) + printColor.END)

    return messages.DONE


if __name__ == "__main__":
    need_print = True
    parser = argparse.ArgumentParser(
        description='Decode base64 from input file to output file.')

    parser.add_argument('-i', '--input', metavar='',
                        help='input file path with base64')
    parser.add_argument('-o', '--output', metavar='', help='output file path')

    args = parser.parse_args()

    inputFile = args.input
    outputFile = args.output

    main(inputFile, outputFile)
