#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-11-22
Purpose: Autoformat Files from campbell scientific for SWGH
"""

import argparse
import sys
import pandas as od


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensivitive search (default: false)',
                        action='store_false')

    parser.add_argument('-o',
                        '--outfile',
                        help='specificy output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('pattern',
                        metavar='str',
                        help='Search pattern')

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Makes Soup"""
    args = get_args()
    imp_csv(args.file)

# --------------------------------------------------


def imp_csv(fh):
    """imports the indicated csv file as a series of lists"""
    tbl = [[]]
    for row in fh:
        for col in row:
            if col == "\n":
                tbl.append([])


    return tbl



# --------------------------------------------------


if __name__ == '__main__':
    main()